#!/usr/bin/env python3
"""Resolve the private Google TTS key in-process; CLI reports readiness only."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Mapping

KEY_NAMES = ("GEMINI_API_KEY", "GOOGLE_API_KEY")


def _read_private_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    if not path.is_file() or path.stat().st_size > 65536:
        raise ValueError("Private key configuration must be a small text file.")
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"(?:export\s+)?(GEMINI_API_KEY|GOOGLE_API_KEY)\s*=\s*(.*)", line)
        if not match:
            raise ValueError("Private key file accepts only Google key assignments/comments.")
        name, value = match.groups()
        value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
        if value.startswith(("'", '"')):
            if len(value) < 2 or value[-1] != value[0]:
                raise ValueError("Private key file has an unmatched quote.")
            value = value[1:-1]
        if value and (re.search(r"\s", value) or any(c in value for c in "$`;")):
            raise ValueError("Private key must be a literal value, not shell syntax.")
        if name in values:
            raise ValueError("Duplicate key assignment in private configuration.")
        values[name] = value
    return values


def resolve_key(
    secret_file: Path | None = None, environ: Mapping[str, str] | None = None
) -> tuple[str, str]:
    """Return (key, source) for direct client use. Never print/log this tuple."""
    skill_root = Path(__file__).resolve().parent.parent
    path = secret_file if secret_file is not None else skill_root / ".secrets/google-tts.env"
    if secret_file is None and not path.resolve().is_relative_to(skill_root):
        raise ValueError("Default private key path must stay inside the skill.")
    values = _read_private_file(Path(path))
    for name in KEY_NAMES:
        if values.get(name):
            return values[name], "skill_private_file"
    env = os.environ if environ is None else environ
    for name in KEY_NAMES:
        value = env.get(name, "").strip()
        if value:
            return value, f"environment:{name}"
    raise ValueError("Google key not configured. Fill the private file or secure environment.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", action="store_true", required=True)
    parser.parse_args()
    try:
        _, source = resolve_key()
    except (OSError, UnicodeError, ValueError):
        print(json.dumps({"ready": False, "source": None, "api_access_verified": False,
                          "note": "Key missing or private configuration invalid; check it locally without printing it."}))
        return 2
    print(json.dumps({"ready": True, "source": source, "api_access_verified": False}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
