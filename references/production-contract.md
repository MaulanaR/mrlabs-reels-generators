# Production state, prompts, and timing

Read when creating or resuming a project. Copy `assets/production.template.json` to the project root as `production.json`. Resolve artifact paths relative to that project root. Keep credentials outside project files.

Resolve the selected style using [style-catalog.json](style-catalog.json). Store its ID and number in `style_profile` and `style_number`. Copy its sample image into `02_visual-references/` when using a project-local `style_preview_path`; this is a style reference, not the full video's background or an authorized presenter identity. Generate DESIGN.md from the chosen palette, fonts, motion, caption, and avoid rules, adapted to actual theme/brand. Keep original demo text out of the new script.

## State and recovery

Use stage: `brief`, `research`, `script`, `awaiting_script_approval`, `voice`, `assets`, `assembly`, `review`, `completed`, or `blocked`. Advance after its artifacts are usable and required approval is valid. Waiting for script approval is a normal writing-stage handoff, not a failed/completed production. The manifest records observed work; it is not a background scheduler.

## Theme and script approval

Read [script-and-assets.md](script-and-assets.md). `theme_contract` keeps the actual subject/message, required visual content, and off-topic exclusions separate from the style catalog. `script_version` and `script_sha256` identify the current saved script. Compute SHA-256 from the actual script file (for example using Get-FileHash or Python hashlib); never fabricate a hash.

Before approval, set `script_approval.status: pending` and `stage: awaiting_script_approval`, show the full narration and storyboard in chat, and wait. Keep approved fields null. On direct user approval, record `approved_version`, `approved_script_sha256`, `approved_at`, and `approval_message` using real evidence. The template starts `not_requested`; an unfilled manifest is never approved.

Require matching current/approved versions and hashes before narration, Gemini images, Flow B-roll, or rendering. If the script changes, mark approval `stale` and return the revision for approval. Reuse valid approval on resume; selecting a style or providing a topic does not count. No media generation may run while approval is missing/pending/stale.

Use [check-script-approval.py](../scripts/check-script-approval.py) before each production submission. Exit 0 means the recorded status, version, actual file hash, and approval fields agree; exit 2 blocks generation. It cannot authenticate chat messages, so the operator must record only a real user's approval. There is deliberately no command that auto-approves a script.

For generated assets record stable asset ID, shot ID, type, source, local path, duration/dimensions, and status. For Flow submissions record exact prompt, observed job/project URL or identifier, attempt number, last observed status, download paths, and rejection reason. Do not invent identifiers the UI does not expose.

Asset states: `planned`, `submitted`, `processing`, `downloaded`, `accepted`, `rejected`, `failed`. On continuation:

1. Read the manifest, actual script, approval/version/hash, shot plan, actual files, and existing remote results. Missing or stale script approval blocks new generation.
2. Probe downloaded/accepted media and verify the selected shot/narration version.
3. Resume incomplete work without regenerating accepted footage or blindly duplicating a submission after a timeout.
4. Invalidate dependent timings/compositions after voice changes; visual changes affect only their dependent stages.
5. Save before required user interaction. Failed assets do not invalidate unrelated successful work.

## Voice artifacts

- `04_voiceover_transcript.md`: authored spoken script.
- `05_tts_request.json`: Google AI Studio TTS provider/interface, actual model/voice, approved spoken text, script version/hash, separate delivery direction, and exact submitted API body or browser settings. Follow [google-ai-studio-tts.md](google-ai-studio-tts.md); keep credentials out of this file.
- `08_voiceover/01_narration.wav`: suggested filename for the selected audio. Keep alternative takes.
- `08_voiceover/words.json`: actual-audio word intervals, for example `[{"text":"Contoh","start":0.2,"end":0.55}]`. Intervals must be chronological, nonnegative, and fit measured audio. Use actual segment intervals if words are unavailable, recording `timing_precision: segment`.

Record the chosen take/version and measured duration. Rebuild shot/caption timing after changing it. Any trimmed/retimed audio needs a matching transcript.

New projects use manifest schema `1.4` with `narration.provider: google_ai_studio_tts`, `interface: auto`, and `billing_mode: free_only`. Resolve `interface` to `api` or `browser` when submitting and record the actual `model_id`, `voice_name`, and non-secret request/result metadata. No local backend health check or speech-model download is needed.

When resuming an older project, preserve its accepted audio, previous request files, and script approval. Update its provider/path metadata when new narration is needed, using `05_tts_request.json`; do not overwrite a legacy VoiceStudio request file or mix settings from different providers. Changing the provider alone does not approve an unseen script or require rewriting an already approved one.

## SFX cues and mixing

Read [sound-design.md](sound-design.md). Copy [sfx-cues.template.json](../assets/sfx-cues.template.json) to `09_edit/sfx-cues.json` during planning. The cue file is the authoritative SFX plan, timing, mix settings, and provenance record; `production.json.audio_design` records its overall state. Register acquired sounds in the manifest's existing `assets` array as `type: sfx`, using the same asset IDs and local paths as the cue file.

The cue-file `schema_version` is independent of the production manifest. Resolve its `style_profile`, script version/hash, selected narration path/hash, measured duration, and composition revision from actual project state. Planned cues have event anchors but null actual times/asset IDs. Before rendering, finalize measured cue intervals and settings, or mark optional unavailable cues `omitted` with a reason. A cue is not accepted media until its linked file decodes and its source/license record is usable.

After narration changes, mark `audio_design.status: needs_retime` and `timing_status: stale` in the cue file; update all dependent cues and the mixed master. After an animation edit, re-resolve affected event anchors. Preserve original TTS audio and use `09_edit/audio_mix.wav` (or the actually chosen format) as a separate mixed master when pre-mixing. Ensure composition playback does not add the same voice/SFX tracks again.

On older manifests without `audio_design`, add these fields only when sound design is needed, retaining accepted assets and script approval. `mode: none` records a user's no-SFX choice and requires no sound download. Keep stock sounds private when their terms prohibit source-file redistribution; provide rendered output and source receipts/re-download information for an external handoff.

## Shot and prompt JSON

`06_flow_prompts.json` contains all ordered scenes, including motion graphics, Gemini images, and raw B-roll. It is a local plan; send individual asset prompts to the matching provider rather than pasting the whole skill into Gemini. A writing-phase plan uses estimated timing, null actual-audio fields, and no invented word indexes. After approval and actual narration, fill measured timing. Example of the measured shape:

```json
{
  "schema_version": "1.2",
  "project_id": "theme-slug",
  "theme": "The actual user topic",
  "script_version": 1,
  "audio_file": "08_voiceover/01_narration.wav",
  "audio_duration_sec": 34.8,
  "timing_precision": "word",
  "shots": [
    {
      "id": "s01",
      "order": 1,
      "start_sec": 0.0,
      "end_sec": 3.4,
      "voiceover_segment": "Exact words from the selected narration take.",
      "word_start_index": 0,
      "word_end_index": 8,
      "core_message": "The one idea this shot explains",
      "subject": "Specific subject required by this approved scene",
      "action": "Observable theme-specific action or state",
      "setting": "Required topic context",
      "visual_type": "motion",
      "role": "explainer",
      "broll_treatment": null,
      "visual_action": "Labeled input travels along a connector and activates the output.",
      "visual_prompt": "Theme-specific editable layout, hierarchy, and reveal behavior.",
      "gemini_prompt": null,
      "flow_prompt": null,
      "reference_images": [],
      "asset_ids": [],
      "avoid": ["unreadable microtext", "unrelated scenery"],
      "transition_out": {"type": "crossfade", "duration_sec": 0.2}
    }
  ]
}
```

These values illustrate fields, not a real script/measurement. Fill actual project values. Use visual_type: `motion`, `image`, `flow` (raw moving B-roll), or `source`. Word indexes are zero-based inclusive indexes in normalized words; omit them for provisional/segment-only timing. Match voiceover_segment to the approved script and actual selected audio. `gemini_prompt` requests one image/illustration asset (or supported raw B-roll capability); `flow_prompt` requests one moving B-roll asset in Flow. Neither requests a complete narrated/captioned Reel.

The example shows one explanatory shot, not a complete production plan. A complete plan must also include at least one qualifying B-roll scene per video as specified below. Use `role: broll` for that scene; for `visual_type: image`, fill `broll_treatment` with its actual planned camera/parallax movement. Other roles can identify explanation, presenter, or title shots without counting them as B-roll.

For each acquired B-roll shot, record a `hyperframes` binding as described in [hyperframes-broll.md](hyperframes-broll.md): actual clip/wrapper IDs, staged source path, source trim, track, visual layer, layout, and framing. Global clip start/duration derive from that shot's measured `start_sec`/`end_sec`; do not maintain a second unrelated timing estimate. The binding must match the final composition HTML. Additive editing metadata does not alter the approved spoken script.

A Flow prompt specifies subject, action, setting, camera/framing, lighting, consistency anchors, and room for overlays. Request clean footage without final labels or narration. Use reference files the project may upload. Put avoidance instructions into supported UI controls or the prompt; do not assume a negative-prompt field exists. Generate a supported duration from the current UI and trim/select it during editing rather than assuming arbitrary exact generation length.

For Gemini, build the per-scene prompt from script-and-assets.md: actual theme, approved narration segment, visual purpose, subject/action/setting, style-only tokens, and exclusions. Do not reuse the catalog sample's demo theme or its sample-generation prompt. Log a content/purpose/style review for each downloaded asset; mismatched subjects fail even if their visual style looks correct.

Final text, captions, metrics, and diagrams remain editable HyperFrames layers. Generated depictions do not prove facts. Illustrative numbers must be clearly illustrative or omitted; factual numbers link to research sources. Consult [current official Flow help](https://support.google.com/flow/answer/16353334) when capabilities differ; do not freeze volatile model/duration options into the skill.

## Minimum B-roll per video

The user's default is at least **one B-roll scene in every finished video**, across all styles and rendering routes. Apply the minimum independently to each deliverable in a batch; B-roll in one output does not cover another. A later explicit user request can change this requirement; style selection, generation failure, unavailable quota, or a `motion` route does not change it.

A qualifying scene is a supporting visual tied to an exact narration segment, showing its relevant subject/action/context. It can be a generated clip, authorized source footage, or a theme-specific generated/supplied image given a purposeful pan/zoom/parallax treatment during editing. An image treatment should make the visual readable and useful, rather than add an imperceptible movement just to fill a count. Pure diagram/typography/card animation, catalog sample posters, presenter-only footage, prompt text, and unused downloads do not satisfy the minimum.

Set `broll_requirement.min_scenes_per_video: 1`. During planning, identify at least one `role: broll` shot with an asset route and appropriate treatment. During production, acquire/review its real asset after script approval and insert it in the final composition. Use sufficient screen time for the action or idea; roughly 2-5 seconds is a starting suggestion, not an imposed minimum duration.

Before completing a video, inspect that interval in the actual final encode. Record qualifying scene IDs in `accepted_scene_ids` and an evidence entry for each output containing `video_path`, `scene_id`, `asset_id`, `clip_id`, `start_sec`, `end_sec`, review notes, and any actual frame/evidence path. Mark `review_status: passed` only when at least one qualifying scene visibly appears and explains the corresponding speech. A planned `role` or accepted source file alone is insufficient. Keep the requirement pending/failed when its visual review is unavailable or unsuccessful.

If a required Flow shot fails, preserve its existing bounded retry and explicit-route rules. A different eligible B-roll route may be used when already permitted by the approved storyboard; diagrams/cards cannot replace the last required B-roll. If the minimum remains unmet, report the specific production blocker and keep `stage` incomplete. On resume, add this requirement to older unfinished projects and preserve the approved spoken script; adding a relevant visual under the existing approved message does not require inventing a new narration or approval.

## Checks before rendering

- Parse JSON using a real parser, such as `python -m json.tool`.
- Verify direct script approval and matching current/approved versions and hashes. Theme/style choices alone are insufficient.
- IDs/order numbers are unique. Used asset IDs resolve to usable local files. Required Flow takes have accepted verified outputs; prompt files alone are not produced footage.
- Each output has at least one planned and acquired qualifying B-roll scene bound to a real local video/image element in its composition. Its track/layer, trim, duration, framing, image movement where applicable, and caption/audio routing follow `hyperframes-broll.md`. After rendering, confirm its actual visible interval and record evidence before marking that output completed.
- All intervals have end > start >= 0 and fit selected narration plus a deliberate short tail. Cover the last spoken word. Model transition overlap explicitly with separate tracks where HyperFrames requires it.
- Captions use the final timing, one visible group at once, with no stale group after its end.
- SFX anchors resolve to the current selected narration/animation; used files are accepted and have recorded source/license information. Optional omissions are explicit, required effects are present, and mixed-master/direct-track routing does not duplicate audio.
- Composition dimensions/fps and actual export agree. Duration follows measured narration and deliberate ending, not a provisional 35-second estimate.

## Review receipts

`11_final/VERIFY.md` records actual commands/results, inspected timestamps/frames, audio review, and fixes. Distinguish measured properties, frame review, and unavailable checks. Note the selected reference profile and timestamped examples showing visuals explain the speech.

When available, loudness tooling can target true peak <= -1 dBTP and approximately -14 to -16 LUFS; these are project mix targets, not asserted platform requirements. Review intelligibility, background ducking, joins, and all SFX event attacks/tails against the final encode. Record audible relevance/sync, mix routing, and any omitted cues. Do not claim listening checks based only on transcripts/metadata.

Deliver the encoded MP4, actual transcript/captions, ordered prompts, editable project, and truthful verification. Installed skills alone do not prove runtime quota, login, local models, browser access, or voice profiles are ready.
