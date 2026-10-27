#!/usr/bin/env python3
"""Read-only Islamic workflow consistency check; never grants human approval."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import runpy
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


class WorkflowError(ValueError):
    """Controlled diagnostic that contains no raw artifact/secret values."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise WorkflowError(message)


def local_file(root: Path, value: object) -> Path:
    _require(isinstance(value, str) and bool(value.strip()), "Missing project-local artifact path.")
    path = (root / value).resolve()
    _require(path.is_relative_to(root), "Artifact path escapes the project.")
    _require(path.is_file(), "Required project-local artifact does not exist.")
    return path


def load(root: Path) -> dict:
    manifest = json.loads((root / "production.json").read_text(encoding="utf-8-sig"))
    _require(isinstance(manifest, dict), "Manifest must be a JSON object.")
    return manifest


def review_digest(root: Path, manifest: dict) -> str:
    paths = manifest.get("review_package", {}).get("files", [])
    files = manifest.get("files", {})
    required = [files.get(k) for k in ("research", "religious_references", "storyboard", "script", "design")]
    _require(isinstance(paths, list) and bool(paths), "Review package files are missing.")
    _require(all(isinstance(p, str) for p in paths), "Review paths must be text.")
    _require(len(set(paths)) == len(paths), "Duplicate review paths are not allowed.")
    _require(all(p and p in paths for p in required), "Review package omits required research/ledger/storyboard/script/design.")
    records = []
    resolved = set()
    for item in sorted(paths):
        path = local_file(root, item)
        _require(not any(part.startswith(".env") or part == ".secrets" for part in path.relative_to(root).parts),
                 "Secret files cannot be review artifacts.")
        _require(path not in resolved, "Duplicate resolved review artifact.")
        resolved.add(path)
        _require(path != (root / str(files.get("review_package", "05_review_package.json"))).resolve(),
                 "Review receipt must not hash itself.")
        records.append({"path": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    credits = manifest.get("credits", {})
    brief = manifest.get("brief", {})
    captions = manifest.get("captions", {})
    narration = manifest.get("narration", {})
    motion = manifest.get("motion", {})
    context = {
        "workflow_mode": manifest.get("workflow_mode"), "theme": manifest.get("theme"),
        "theme_contract": manifest.get("theme_contract"), "style_profile": manifest.get("style_profile"),
        "content_policy": manifest.get("content_policy"), "religious_references": manifest.get("religious_references"),
        "credits": {k: credits.get(k) for k in ("instagram_username", "cta", "duration_sec")},
        "brief": {k: brief.get(k) for k in ("language", "target_duration_sec", "width", "height", "fps")},
        "captions": {k: captions.get(k) for k in ("enabled", "max_lines", "border_radius_px", "border_style", "timing")},
        "motion": {k: motion.get(k) for k in ("priority", "engine", "threejs", "clock", "smooth")},
        "narration": {k: narration.get(k) for k in ("mode", "provider", "execution", "quran_audio", "allow_local_generation", "automatic_fallback")},
        "duration_policy": manifest.get("platforms", {}).get("duration_policy"),
        "visual_production": manifest.get("visual_production"),
    }
    raw = json.dumps({"artifacts": records, "context": context}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def check_references(root: Path, manifest: dict) -> None:
    ledger = json.loads(local_file(root, manifest.get("files", {}).get("religious_references")).read_text(encoding="utf-8-sig"))
    _require(isinstance(ledger, dict) and ledger == manifest.get("religious_references"),
             "Religious ledger and manifest record must agree.")
    _require(ledger.get("status") == "verified", "Religious research is pending/unverified.")
    claims = ledger.get("claims")
    _require(isinstance(claims, list), "Religious claims must be a list.")
    if not claims:
        _require(bool(ledger.get("review_notes")), "An empty claim ledger needs an honest reviewed explanation.")
    seen = set()
    for claim in claims:
        _require(isinstance(claim, dict), "Each religious claim must be an object.")
        cid = claim.get("id")
        _require(isinstance(cid, str) and bool(cid.strip()) and cid not in seen, "Claim IDs must be unique and nonempty.")
        seen.add(cid)
        _require(claim.get("status") == "verified", "A religious claim remains unverified.")
        for key in ("claim", "kind", "source_url", "context"):
            _require(isinstance(claim.get(key), str) and bool(claim[key].strip()), "A claim is missing source/context fields.")
        _require(claim["source_url"].startswith(("https://", "http://")), "A claim needs its actual source URL.")
        kind = claim["kind"]
        _require(kind in {"quran", "hadith", "tafsir", "history", "reflection"}, "Unknown religious source kind.")
        if kind == "quran":
            _require(all(claim.get(k) for k in ("surah", "verses", "translation_source")), "Quran claim needs surah/verses/translation source.")
        if kind == "hadith":
            _require(all(claim.get(k) for k in ("collection", "number", "numbering_edition", "grading_authority")),
                     "Hadith needs collection/number/edition/grading authority.")
            _require(claim.get("grade") in {"sahih", "hasan"}, "Hadith grade is not verified sahih/hasan under this policy.")


def classify_youtube(duration: float) -> str:
    _require(math.isfinite(duration) and duration > 0, "Final duration must be a finite positive measurement.")
    return "shorts_by_duration" if duration <= 180 else "vertical_video"


def _probe(path: Path) -> dict:
    binary = shutil.which("ffprobe")
    _require(binary is not None, "ffprobe is unavailable; final-media checks cannot be claimed.")
    result = subprocess.run([binary, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)],
                            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    _require(result.returncode == 0, "ffprobe could not read the final media.")
    return json.loads(result.stdout)


def check(root: Path, final: bool = False) -> dict:
    root = root.resolve()
    m = load(root)
    _require(m.get("schema_version") == "1.9", "Expected animation-first Islamic schema 1.9; migrate the reviewed visual plan explicitly.")
    visual = m.get("visual_production", {})
    _require(visual.get("mode") == "hyperframes_animation" and visual.get("broll_enabled") is False and
             visual.get("stock_footage_enabled") is False, "This skill uses authored HyperFrames animation without B-roll/stock cutaways.")
    _require("broll_requirement" not in m, "Remove the retired B-roll requirement when migrating the visual plan.")
    _require(m.get("workflow_mode") in {"theme_to_reel", "source_video_edit"}, "Unknown workflow mode.")
    policy = m.get("content_policy", {})
    expected = {"no_faces": True, "faceless_figures_allowed": True, "prophets": "abstract_light_and_editable_name_only",
                "depict_allah": False, "unseen_visuals": "illustrative_not_literal", "quran_audio": "indonesian_meaning_only",
                "music_allowed": False, "arabic_text": "verified_editable_rtl"}
    _require(all((policy.get(k) is v) if isinstance(v, bool) else (policy.get(k) == v)
                 for k, v in expected.items()), "Islamic visual/audio policies are missing or changed.")
    _require(m.get("audio_design", {}).get("music_allowed") is False, "Music must be disabled in audio design.")
    credit = m.get("credits", {})
    handle = credit.get("instagram_username")
    _require(isinstance(handle, str) and re.fullmatch(r"@?[A-Za-z0-9._]{1,30}", handle) is not None,
             "Provide the actual Instagram username before production.")
    _require(credit.get("cta") == "Like & share jika bermanfaat.", "Closing CTA differs from the approved policy.")
    edit = m.get("editing", {})
    _require(edit.get("selection_status") == "selected" and edit.get("mode") == "hyperframes" and
             edit.get("engines") == ["hyperframes"] and edit.get("final_assembler") == "hyperframes",
             "This skill uses the preselected HyperFrames route.")
    brief = m.get("brief", {})
    _require((brief.get("width"), brief.get("height"), brief.get("fps")) == (1080, 1920, 30),
             "Expected portrait 1080x1920 at 30 fps.")
    motion = m.get("motion", {})
    _require(motion.get("priority") == "3d" and motion.get("engine") == "hyperframes" and motion.get("smooth") is True,
             "Smooth 3D-priority HyperFrames direction must be retained.")
    caps = m.get("captions", {})
    _require(caps.get("enabled") is True and type(caps.get("max_lines")) is int and 1 <= caps["max_lines"] <= 2 and
             isinstance(caps.get("border_radius_px"), (int, float)) and 18 <= caps["border_radius_px"] <= 30,
             "Rounded readable caption defaults must be retained.")
    voice = m.get("narration", {})
    _require(voice.get("allow_local_generation") is False and voice.get("automatic_fallback") == "none",
             "Local synthesis/automatic fallback is prohibited.")
    mode = voice.get("mode")
    if mode == "tts":
        _require(voice.get("provider") == "google_ai_studio_tts" and voice.get("execution") == "online" and
                 voice.get("quran_audio") == "indonesian_meaning_only", "New speech must be online Google Indonesian meaning, no AI tilawah.")
    else:
        _require(m.get("workflow_mode") == "source_video_edit" and mode in {"source_audio", "none"},
                 "Non-TTS modes require an actual source-video workflow.")
        _require(bool(m.get("source_video", {}).get("files")), "Source mode needs recorded input identities.")
        if mode == "source_audio":
            _require(voice.get("provider") == "source_media" and voice.get("execution") == "imported",
                     "Source speech must be identified as imported original media.")
    _require(m.get("platforms", {}).get("duration_policy") == "follow_discussion_keep_full", "Full discussion duration must be preserved.")
    check_references(root, m)
    original_check = runpy.run_path(str(Path(__file__).with_name("check-script-approval.py")))["check"]
    try:
        original_check(root)
    except (ValueError, OSError, TypeError, AttributeError) as error:
        raise WorkflowError("Script approval is missing, stale or inconsistent; show the actual revision to the user.") from error
    digest = review_digest(root, m)
    _require(m.get("review_package", {}).get("approved_sha256") == digest,
             "Reviewed package changed or its genuine human approval digest is missing.")
    result = {"allowed": True, "scope": "final" if final else "production", "review_package_sha256": digest,
              "note": "Recorded consistency only; real human approval, research and actual media review are still required."}
    if not final:
        return result
    reviews = m.get("policy_review", {})
    _require(reviews.get("status") == "passed" and all(reviews.get(k) is True for k in
             ("no_faces", "prophets_symbolic", "no_music", "source_and_dalil_checked")) and bool(reviews.get("evidence")),
             "Final face/prophet/music/source review or real evidence remains incomplete.")
    for section in ("captions", "motion", "credits", "audio_design"):
        _require(m.get(section, {}).get("review_status") == "passed", "A required final component review is incomplete.")
    _require(m.get("quality", {}).get("status") == "passed", "Final quality review is incomplete.")
    _require(m.get("motion", {}).get("webgl_capture_status") in {"passed", "not_used"}, "Report actual WebGL capture status.")
    local_file(root, m.get("files", {}).get("verification"))
    video = local_file(root, m.get("final_video_path"))
    probe = _probe(video)
    videos = [s for s in probe.get("streams", []) if s.get("codec_type") == "video"]
    audios = [s for s in probe.get("streams", []) if s.get("codec_type") == "audio"]
    _require(bool(videos), "Final video stream is missing.")
    v = videos[0]
    _require(v.get("codec_name") == "h264" and (v.get("width"), v.get("height")) == (1080, 1920),
             "Final video must be portrait 1080x1920 H.264.")
    _require(abs(float(Fraction(v.get("avg_frame_rate", "0/1"))) - 30) < .01, "Final fps differs from 30.")
    rotations = [float(v.get("tags", {}).get("rotate", 0))] + [float(d.get("rotation", 0)) for d in v.get("side_data_list", [])]
    _require(all(rotation % 360 == 0 for rotation in rotations), "Output has rotation metadata inconsistent with portrait dimensions.")
    _require(all(s.get("codec_name") == "aac" for s in audios), "Final audio must be AAC.")
    _require(bool(audios) or mode == "none", "Required narration audio stream is missing.")
    duration = float(probe.get("format", {}).get("duration", 0))
    classification = classify_youtube(duration)
    _require(m.get("platforms", {}).get("youtube_classification") == classification, "YouTube classification does not match actual full duration.")
    _require(m.get("platforms", {}).get("instagram_status") in {"not_verified", "compatible", "not_compatible"},
             "Record actual Instagram verification status without inventing compatibility.")
    result.update(measured_duration_sec=duration, youtube_classification=classification)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--digest", action="store_true")
    group.add_argument("--final", action="store_true")
    args = parser.parse_args()
    try:
        root = args.project.resolve()
        result = ({"review_package_sha256": review_digest(root, load(root)), "note": "Read-only digest; not approval."}
                  if args.digest else check(root, args.final))
    except (OSError, ValueError, TypeError, KeyError, AttributeError, ZeroDivisionError, subprocess.SubprocessError) as error:
        # Do not dump file contents, subprocess stderr or secret-bearing exception context.
        reason = str(error) if isinstance(error, WorkflowError) else "Invalid/missing project metadata or media; inspect it locally without printing secrets."
        print(json.dumps({"allowed": False, "reason": reason}), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
