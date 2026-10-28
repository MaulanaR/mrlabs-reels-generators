# Production state and acceptance contract

Schema `1.10` specializes the standalone skill for authored HyperFrames animation without changing parent projects. Copy `assets/production.template.json`. Paths are project-relative except the private credential file, which is skill-relative. No credential values belong in this manifest.

## Mode, policy and editor

Default `workflow_mode: theme_to_reel`; optional `source_video_edit` needs an explicitly supplied source. Stages: `brief`, `research`, `script`, `awaiting_script_approval`, `voice`, `sample`, `awaiting_sample_approval`, `assets`, `assembly`, `review`, `completed`, `blocked`. Missing inputs/verification never mean completed.

`editing` already selects HyperFrames under this skill's user-requested configuration. Keep `engines: ["hyperframes"]`, mode/final_assembler `hyperframes`. Three.js is a scene renderer, not another editor choice. Keep actual stage/job metadata without invoking other engines automatically.

Keep `content_policy` consistent: no faces, faceless figures allowed, prophets only abstract light with an editable centered name, no depiction of Allah, unseen imagery illustrative, Quran audio Indonesian meaning only, no music, verified editable RTL Arabic. `motion.priority: 3d` is retained. The main scene is a grounded spatial world as defined in `reference-analysis.md`; do not replace it with flat SVG/card slides or mislabel 2.5D.

## Sources and approval package

Read `religious-research.md`. Save the same status/claims/review_notes in `01_religious_references.json` and manifest `religious_references`. Mark verified only after checking real sources. Pending/unverifiable material blocks production. Claim fields are defined in that reference.

The inherited `script_version`, real script SHA-256 and `script_approval` fields/checker remain unchanged. `files.script` is the actual spoken script, or `04_edit_review.md` in source mode. No invented narration is required for a recording.

`review_package.files` contains actual project-local research, religious-source JSON, storyboard, script/review artifact and DESIGN.md. No duplicates, secret files, path escapes or nonexistent documents. In source mode replace the script entry with its actual review path and freeze source identities/cuts in that artifact. All required review documents must be included.

`workflow_guard.py --digest` hashes sorted actual file paths/bytes plus reviewed context: theme/workflow, actual credits, policies, religious ledger, selected profile, portrait/caption/motion direction narration mode/provider and `visual_production`, plus the sample duration/purpose policy. Mutable sample receipts/approval are excluded from the package digest to avoid self-reference. It never approves or writes anything. On genuine human approval record the script approval and returned package digest in `review_package.approved_sha256`. Save the receipt in `05_review_package.json`; do not include that receipt in its own hash list.

Normal guard checks script approval and package digest. A material change to research, sources, storyboard, design, credit, policy or spoken script makes the package stale and needs approval of the revised concrete package. Put technical timing/crop/layout repairs in separate working metadata without rewriting frozen review artifacts. Do not record model/tool text as approval.

`credits.instagram_username` is a supplied actual handle, with optional leading @. Show it in review. CTA is exactly `Like & share jika bermanfaat.` The roughly five-second closing must remain readable. No guessed account or religious engagement promises.

## Audio, timing and scene records

New speech: `narration.mode: tts`, Google AI Studio TTS, online, no local generation/fallback, actual supported model/voice and confirmed free-only access until separately authorized. Secret resolution is in `google-ai-studio-tts.md`. No key in request/manifest artifacts.

Source recording: `source_audio`/`source_media`/`imported` references actual supplied speech/stream and reviewed EDL; `none` invents no speech. Clear unused cloud fields and skip TTS setup. Original audio must still meet religious/no-music policies. No original-face exemption.

Create `05_tts_request.json` only for requested TTS: exact approved Indonesian meaning/explanation, separate delivery direction, script version/hash, actual settings and non-secret observed identifiers. No AI tilawah. Inspect response MIME/encoding, save actual returned audio, probe/listen and retain alternatives. Local conversion/mixing is allowed; local synthesis is not.

Actual selected audio or retimed EDL controls every animated scene, caption, motion and SFX cue. Use real word/segment boundaries, never evenly distributed fake word times. Rebuild dependencies after audio/cut changes.

`06_scene_assets.json`: ordered shot IDs; actual or explicitly provisional times; exact narration; subject/action/setting; background profile; actual visual action/method (main `threejs_3d`/`authored_3d_prerender`, secondary `css_2_5d`/`svg_animation` overlays, or explicitly supplied `source_video`); source-claim IDs; role; asset route; actual accepted asset IDs and HyperFrames binding. A prophet marker needs its verified name/text ID and `representation: abstract_light_only`; no generated lettering/body. No invented completed assets during writing.

Optional scene resources go in `07_scene_assets/`, selected voice in `08_voiceover/`, SFX cues/files under `09_edit/` and runtime copies under `10_editing/hyperframes/assets/`. Binding/timing/layering follow `hyperframes-animation.md`. Record provenance/license/attribution and actual asset hashes/properties when an external resource is used. Procedural objects need actual component/source bindings, not fictitious stock receipts.

## Authored animation, no B-roll requirement

`visual_production` is `mode: hyperframes_animation`, `broll_enabled: false`, `stock_footage_enabled: false`. Its `visual_target.style` is `grounded_stylized_spatial_3d`, `fallback_policy` is `report_blocker_no_silent_flat_substitution`, and `main_scene_method` is `threejs_3d` (or an explicitly reviewed `authored_3d_prerender`). `background_strategy` selects contextual scene variants with continuity. These fields are included in the approval digest. Build contextual objects/environments/diagrams/editable text with smooth purposeful motion. No B-roll acquisition, download/generation sequence, insertion step, minimum clip count, accepted-scene list or B-roll evidence is required. Do not import the parent's B-roll gate. An entirely procedural animated video is valid; it must still satisfy actual animation, caption, audio, policy and encoded review.

For existing projects with the old visual plan (including schema 1.8/1.9 defaults), preserve original files/receipts and approved history. Copy/update working metadata to schema 1.10, replace the old sourcing plan with authored animated scenes, remove `broll_requirement` and source feature `broll`, replace `files.broll_assets` with `files.scene_assets`, and apply the current `asset_generation`/`visual_production` template. Do not delete accepted legacy media automatically or silently render a previously approved stock plan under the new workflow. Show the revised concrete storyboard/design and obtain genuine approval if the reviewed visual plan changes. The package digest now includes visual-production direction, so recalculate it only after real approval; never auto-approve a migration or reuse a stale digest. Add the new sample state and separate art-review paths from the template. An older completed render/technical pass is not sample acceptance; only carry forward an actual prior explicit acceptance of the same encoded sample/package, if one exists.

## Representative sample and full-render gate

Follow `visual-quality.md`. `visual_sample.target_duration_sec: [8, 12]` and its representative purpose are frozen review context. Script approval permits preparation and production of this sample, not automatic full-length production. The sample uses an actual approved narration/source interval and intended final portrait/caption/audio treatment.

- `visual_sample.video_path` points to the actual encoded sample, `media_sha256` is its real SHA-256, and `source_interval_sec.start/end` records its actual approved audio excerpt. The guard probes H.264 1080x1920/30 fps, actual 8-12 second duration with encoding tolerance, and intended narration audio presence.
- Copy `assets/visual-review.template.json` to `visual_sample.review_path` (default `10_editing/lookdev/visual-review.json`), set `scope: sample` and bind it to the actual media path/hash and current `review_package.approved_sha256`.
- A review needs a real reference comparison and at least three distinct, chronologically timed local image files from the encoded before/action/result sequence. Seven criteria (`asset_quality`, `action_clarity`, `composition`, `materials_and_lighting`, `pacing_and_camera`, `caption_legibility`, `reference_match`) have honest statuses, concrete findings and local encoded/frame evidence paths. A pending/needs-work criterion blocks the full-render gate.
- After the user explicitly accepts the shown sample, record `visual_sample.approval.status: approved`, the actual `approval_message`/`approved_at`, `approved_media_sha256`, `approved_review_sha256` (SHA-256 of the review JSON's bytes) and `approved_review_package_sha256`. A rejected/pending sample does not authorize full rendering; script approval, a gallery selection or an agent/tool response cannot stand in for sample acceptance.

`workflow_guard.py <project>` checks the script package for preparation/sample production. If the manifest stage is already `assets`, `assembly`, `review` or `completed`, it also enforces sample acceptance even without the full-render flag. Use `sample`/`awaiting_sample_approval` for the limited sample work; the `assets` stage refers to full-video asset expansion. `--full-render` additionally checks the encoded sample, review evidence, hashes and recorded sample acceptance before full-length asset expansion, animation/prerender and assembly. `--final` also requires this accepted sample, then validates the separate final output. Neither mode authenticates human messages or automatically decides artistic quality.

If a sample's bytes, review receipt or approved script/design package changes, its old acceptance is stale. Show the concrete revision; do not silently recalculate approved hashes. Reuse a genuinely accepted unchanged sample on resume. Keep technical work outside the frozen script/design artifacts where appropriate, but do not use that distinction to hide a material visual downgrade.

## Final review and classification

Review actual output, not just lint/source. Save `11_final/VERIFY.md` with real commands, measured streams/timecodes, face-sensitive frames/camera turns, prophet/name, Arabic/captions, source/voice provenance, animated scene action/seek checks, SFX/music listening, credit and limitations. A detector/thumbnail is not an exhaustive face check; a waveform/transcript is not a listening review.

Required final records (never fabricate them to pass):

- The genuinely accepted representative sample and its bound review/approval records described above.
- A separate `quality.art_review_path` (default `11_final/visual-review.json`) with `scope: final`, actual final MP4 path/hash, current approved package hash, three or more real frame samples and all seven artistic criteria with findings/evidence. The guard rejects a sample receipt reused as a final review. Inspect every final scene/important transition; three sampled images alone do not prove exhaustive review.

- `policy_review.status: passed`; booleans `no_faces`, `prophets_symbolic`, `no_music`, `source_and_dalil_checked: true`; nonempty actual evidence notes/paths. No prophet scene records not-applicable review in its notes.
- Caption, motion, credit, audio_design review statuses and `quality.status: passed`. `motion.webgl_capture_status` is `passed` with actual capture evidence or `not_used` for non-WebGL work, with the true motion method recorded. Main `threejs_3d` scenes require `webgl_capture_status: passed` from actual HyperFrames capture; standalone gallery PNGs are insufficient. An `authored_3d_prerender` route requires actual `motion.prerender_evidence` describing editable source, export and integration review. Flags/notes alone cannot prove the underlying check.
- Real final MP4 and VERIFY path; actual animated-scene/transition/seek evidence in motion/quality review. `platforms.youtube_classification` is `shorts_by_duration` for measured final duration <=180 seconds, otherwise `vertical_video`. Duration alone is not all-platform eligibility.
- `platforms.instagram_status`: `not_verified`, `compatible` or `not_compatible`; record route/limits/date if actually checked. Unknown limits do not justify truncating the master or claiming upload compatibility.

Run `workflow_guard.py <project> --final` before completion. It also probes actual final dimensions/fps/duration/codecs with ffprobe. A pass proves recorded consistency/probe checks, not authentic research/approval or semantic face/music absence; operator review remains necessary. Deliver full portrait MP4, subtitles/timings, editable source, approved writing/research/dalil and rights receipts, without automatic publication.
