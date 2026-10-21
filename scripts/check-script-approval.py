#!/usr/bin/env python3
"""Read-only approval check before producing media for a Reel project."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def check(project: Path) -> dict:
    root = project.resolve()
    manifest = json.loads((root / "production.json").read_text(encoding="utf-8-sig"))
    approval = manifest.get("script_approval") or {}
    if approval.get("status") != "approved":
        raise ValueError("Script approval is missing, pending, or stale. Present the script and wait for the user.")

    version = manifest.get("script_version")
    if type(version) is not int or version < 1:
        raise ValueError("The current script_version must be a positive integer.")
    if type(approval.get("approved_version")) is not int or approval["approved_version"] != version:
        raise ValueError("Approval belongs to a different script version. Request approval for the current version.")

    script_relative = (manifest.get("files") or {}).get("script")
    if not isinstance(script_relative, str) or not script_relative.strip():
        raise ValueError("The manifest is missing files.script.")
    script = (root / script_relative).resolve()
    if not script.is_relative_to(root):
        raise ValueError("The script must be a project-local artifact.")
    raw = script.read_bytes()
    if not raw.decode("utf-8-sig").strip():
        raise ValueError("The script is empty.")
    actual = hashlib.sha256(raw).hexdigest()
    recorded_hash = manifest.get("script_sha256")
    if not isinstance(recorded_hash, str) or recorded_hash.strip().lower() != actual:
        raise ValueError("The saved script changed after its recorded hash. Revise the writing/approval state first.")
    approved_hash = approval.get("approved_script_sha256")
    if not isinstance(approved_hash, str) or approved_hash.strip().lower() != actual:
        raise ValueError("The actual script does not match the user-approved script. Fresh approval is required.")

    for field in ("approval_message", "approved_at"):
        value = approval.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Missing {field}; record actual user approval evidence, never fabricate it.")

    return {
        "allowed": True,
        "script_version": version,
        "script_sha256": actual,
        "script": str(script),
        "note": "Checks recorded approval consistency; the approval message must come from the human user.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Reel project directory containing production.json")
    args = parser.parse_args()
    try:
        result = check(args.project)
    except (OSError, ValueError, TypeError, AttributeError) as error:
        print(json.dumps({"allowed": False, "reason": str(error)}, ensure_ascii=True), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
