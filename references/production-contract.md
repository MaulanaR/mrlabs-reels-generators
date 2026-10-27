# Production state and acceptance contract

Schema `1.8` extends the parent fields without changing parent projects. Copy `assets/production.template.json`. Paths are project-relative except the private credential file, which is skill-relative. No credential values belong in this manifest.

## Mode, policy and editor

Default `workflow_mode: theme_to_reel`; optional `source_video_edit` needs an explicitly supplied source. Stages: `brief`, `research`, `script`, `awaiting_script_approval`, `voice`, `assets`, `assembly`, `review`, `completed`, `blocked`. Missing inputs/verification never mean completed.

`editing` already selects HyperFrames under this skill's user-requested configuration. Keep `engines: ["hyperframes"]`, mode/final_assembler `hyperframes`. Three.js is a scene renderer, not another editor choice. Keep actual stage/job metadata without invoking other engines automatically.

Keep `content_policy` consistent: no faces, faceless figures allowed, prophets only abstract light with an editable centered name, no depiction of Allah, unseen imagery illustrative, Quran audio Indonesian meaning only, no music, verified editable RTL Arabic. `motion.priority: 3d` prioritizes useful supported 3D; never mislabel 2.5D.

## Sources and approval package

Read `religious-research.md`. Save the same status/claims/review_notes in `01_religious_references.json` and manifest `religious_references`. Mark verified only after checking real sources. Pending/unverifiable material blocks production. Claim fields are defined in that reference.

The inherited `script_version`, real script SHA-256 and `script_approval` fields/checker remain unchanged. `files.script` is the actual spoken script, or `04_edit_review.md` in source mode. No invented narration is required for a recording.

`review_package.files` contains actual project-local research, religious-source JSON, storyboard, script/review artifact and DESIGN.md. No duplicates, secret files, path escapes or nonexistent documents. In source mode replace the script entry with its actual review path and freeze source identities/cuts in that artifact. All required review documents must be included.

`workflow_guard.py --digest` hashes sorted actual file paths/bytes plus reviewed context: theme/workflow, actual credits, policies, religious ledger, selected profile, portrait/caption/motion direction and narration mode/provider. It never approves or writes anything. On genuine human approval record the script approval and returned package digest in `review_package.approved_sha256`. Save the receipt in `05_review_package.json`; do not include that receipt in its own hash list.

Normal guard checks script approval and package digest. A material change to research, sources, storyboard, design, credit, policy or spoken script makes the package stale and needs approval of the revised concrete package. Put technical timing/crop/layout repairs in separate working metadata without rewriting frozen review artifacts. Do not record model/tool text as approval.

`credits.instagram_username` is a supplied actual handle, with optional leading @. Show it in review. CTA is exactly `Like & share jika bermanfaat.` The roughly five-second closing must remain readable. No guessed account or religious engagement promises.

## Audio, timing and scene records

New speech: `narration.mode: tts`, Google AI Studio TTS, online, no local generation/fallback, actual supported model/voice and confirmed free-only access until separately authorized. Secret resolution is in `google-ai-studio-tts.md`. No key in request/manifest artifacts.

Source recording: `source_audio`/`source_media`/`imported` references actual supplied speech/stream and reviewed EDL; `none` invents no speech. Clear unused cloud fields and skip TTS setup. Original audio must still meet religious/no-music policies. No original-face exemption.

Create `05_tts_request.json` only for requested TTS: exact approved Indonesian meaning/explanation, separate delivery direction, script version/hash, actual settings and non-secret observed identifiers. No AI tilawah. Inspect response MIME/encoding, save actual returned audio, probe/listen and retain alternatives. Local conversion/mixing is allowed; local synthesis is not.

Actual selected audio or retimed EDL controls every scene, caption, motion, B-roll and SFX cue. Use real word/segment boundaries, never evenly distributed fake word times. Rebuild dependencies after audio/cut changes.

`06_scene_assets.json`: ordered shot IDs; actual or explicitly provisional times; exact narration; subject/action/setting; background profile; actual visual action/method (`threejs_3d`, `css_2_5d`, `footage`, etc.); source-claim IDs; role; asset route; actual accepted asset IDs and HyperFrames binding. A prophet marker needs its verified name/text ID and `representation: abstract_light_only`; no generated lettering/body. No invented completed assets during writing.

Original B-roll goes in `07_broll_assets/`, selected voice in `08_voiceover/`, SFX cues/files under `09_edit/` and render copies under `10_editing/hyperframes/assets/`. Actual media binding/trim/layers follow `hyperframes-broll.md`. Record asset IDs/hashes/properties, source/license/attribution and content/face review. Prohibited originals may be quarantined evidence but cannot appear unchanged in renders/active previews.

## Minimum B-roll per video

Every complete deliverable needs at least one supporting visual tied to the narration's actual subject/action. Prefer authorized user/internet footage; a sourced still or justified generated image qualifies with purposeful visible movement. Main presenter footage, pure diagram/type animation, style previews, prompts and unused downloads do not count.

After actual encoded review, fill `broll_requirement.accepted_scene_ids`, `review_status: passed` and evidence: video path, scene/asset/clip ID, actual start/end, inspected frames/notes. Check entry/middle/exit, caption visibility and voice continuity. A narrowly requested future subtitle-only operation may explicitly override the minimum; default complete content remains one or more scenes.

## Final review and classification

Review actual output, not just lint/source. Save `11_final/VERIFY.md` with real commands, measured streams/timecodes, face-sensitive frames/camera turns, prophet/name, Arabic/captions, source/voice provenance, B-roll, SFX/music listening, credit and limitations. A detector/thumbnail is not an exhaustive face check; a waveform/transcript is not a listening review.

Required final records (never fabricate them to pass):

- `policy_review.status: passed`; booleans `no_faces`, `prophets_symbolic`, `no_music`, `source_and_dalil_checked: true`; nonempty actual evidence notes/paths. No prophet scene records not-applicable review in its notes.
- Caption, motion, credit, audio_design review statuses and `quality.status: passed`. `motion.webgl_capture_status` is `passed` with actual capture evidence or `not_used` for non-WebGL work, with the true motion method recorded.
- Real final MP4 and VERIFY path; accepted B-roll evidence. `platforms.youtube_classification` is `shorts_by_duration` for measured final duration <=180 seconds, otherwise `vertical_video`. Duration alone is not all-platform eligibility.
- `platforms.instagram_status`: `not_verified`, `compatible` or `not_compatible`; record route/limits/date if actually checked. Unknown limits do not justify truncating the master or claiming upload compatibility.

Run `workflow_guard.py <project> --final` before completion. It also probes actual final dimensions/fps/duration/codecs with ffprobe. A pass proves recorded consistency/probe checks, not authentic research/approval or semantic face/music absence; operator review remains necessary. Deliver full portrait MP4, subtitles/timings, editable source, approved writing/research/dalil and rights receipts, without automatic publication.
