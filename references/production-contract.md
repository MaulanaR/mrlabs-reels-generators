# Production state, prompts, and timing

Read when creating or resuming a project. Copy `assets/production.template.json` to the project root as `production.json`. Resolve artifact paths relative to that project root. Keep credentials outside project files.

Resolve the selected style using [style-catalog.json](style-catalog.json). Store its ID and number in `style_profile` and `style_number`. Copy its sample image into `02_visual-references/` when using a project-local `style_preview_path`; this is a style reference, not the full video's background or an authorized presenter identity. Generate DESIGN.md from the chosen palette, fonts, motion, caption, and avoid rules, adapted to actual theme/brand. Keep original demo text out of the new script.

## State and recovery

Use stage: `brief`, `research`, `script`, `awaiting_script_approval`, `awaiting_editor_choice`, `voice`, `assets`, `assembly`, `review`, `completed`, or `blocked`. Advance after its artifacts are usable and required approval is valid. Waiting for script approval/editor choice is a normal planning handoff, not a failed/completed production. The manifest records observed work; it is not a background scheduler.

## Editing selection and state

New projects use manifest schema `1.7` with `workflow_mode: theme_to_reel` or `source_video_edit`. Follow [editing-options.md](editing-options.md): record the user's actual editor selection in `editing.selection_status`, `selection_message`, `mode`, and `engines`; support Higgsfield, HyperFrames, Remotion, any pair, or all three. Choose exactly one selected `final_assembler` and describe combined-stage jobs in the review package. The template keeps selection pending and `files.composition: null`; fill actual project paths/entry points only after selection. A style's `render_route` describes its visual asset mix, not the editing engine.

Use `editing.project_paths`, `stages`, `handoffs`, and `jobs` for actual editor state. New folders live under `10_editing/<engine>/`; preserve existing project paths. Each handoff records the real export, properties, hash, destination, trim/offset, and caption/audio ownership. No media production starts with pending editor selection, even if script approval has already passed. The script checker only validates the script approval fields; verify editor selection and online narration policy separately.

On older projects, preserve accepted files and script approval. Reuse a documented user editor choice, otherwise ask; a legacy `10_hyperframes/` path is not selection evidence. Never submit new local TTS from an old manifest or companion skill. Changing editor or replacing a noncompliant voice take does not require rewriting an unchanged approved script, but timing/captions/SFX must follow the new selected media.

## Theme and script approval

For `source_video_edit`, follow [source-video-edit.md](source-video-edit.md). Record exact source identities/hashes/properties, selected audio streams and actual transcript paths in `source_video`; keep original and output transcripts distinct. Set `files.script: 04_edit_review.md`, containing the real selected transcript and complete proposed cuts, information, subtitles, motion, B-roll and any requested spoken additions. The existing version/hash/`script_approval` fields and checker validate this review artifact without inventing a new narration. Before render also verify sources/EDL match the approved review. `source_video.edl_path` maps source intervals to output intervals; all cues/captions derive from this map after cuts. Technical sync corrections stay in separate metadata rather than mutating the approved review artifact.

Read [script-and-assets.md](script-and-assets.md). `theme_contract` keeps the actual subject/message, required visual content, and off-topic exclusions separate from the style catalog. `script_version` and `script_sha256` identify the current saved script. Compute SHA-256 from the actual script file (for example using Get-FileHash or Python hashlib); never fabricate a hash.

Before approval, set `script_approval.status: pending` and `stage: awaiting_script_approval`, show the full narration and storyboard in chat, and wait. Keep approved fields null. On direct user approval, record `approved_version`, `approved_script_sha256`, `approved_at`, and `approval_message` using real evidence. The template starts `not_requested`; an unfilled manifest is never approved.

Require matching current/approved versions and hashes before narration, production B-roll/SFX downloads, optional image generation, or rendering. If the script changes, mark approval `stale` and return the revision for approval. Reuse valid approval on resume; selecting a style or providing a topic does not count. No media production may run while approval is missing/pending/stale.

Use [check-script-approval.py](../scripts/check-script-approval.py) before each production submission. Exit 0 means the recorded status, version, actual file hash, and approval fields agree; exit 2 blocks generation. It cannot authenticate chat messages, so the operator must record only a real user's approval. There is deliberately no command that auto-approves a script.

For all acquired/generated assets record stable asset ID, shot ID, type, source, local path, duration/dimensions, and status. Internet assets require the provenance/license fields in [internet-broll.md](internet-broll.md). For an optional imagegen fallback, record the sourcing outcome, fallback reason, exact submitted prompt, observed result path/ID, attempts, and rejection reason when relevant. Do not invent provider identifiers or output paths.

Asset states: `planned`, `submitted`, `processing`, `downloaded`, `accepted`, `rejected`, `failed`. On continuation:

1. Read the manifest, actual script, approval/version/hash, shot plan, actual files, and existing remote results. Missing or stale script approval blocks new generation.
2. Probe downloaded/accepted media and verify the selected shot/narration version.
3. Resume incomplete work without regenerating accepted footage or blindly duplicating a submission after a timeout.
4. Invalidate dependent timings/compositions after voice changes; visual changes affect only their dependent stages.
5. Save before required user interaction. Failed assets do not invalidate unrelated successful work.

## Voice artifacts

The following TTS filenames are theme-mode defaults, not requirements for source editing. In source mode, record real source/stream references and source/output transcript paths; `files.script` points to the approved `04_edit_review.md`. Create no TTS request or invented voice file when keeping original audio.

- `04_voiceover_transcript.md`: authored spoken script.
- `05_tts_request.json`: Google AI Studio TTS provider/interface, actual model/voice, approved spoken text, script version/hash, separate delivery direction, and exact submitted API body or browser settings. Follow [google-ai-studio-tts.md](google-ai-studio-tts.md); keep credentials out of this file.
- `08_voiceover/01_narration.wav`: suggested filename for the selected audio. Keep alternative takes.
- `08_voiceover/words.json`: actual-audio word intervals, for example `[{"text":"Contoh","start":0.2,"end":0.55}]`. Intervals must be chronological, nonnegative, and fit measured audio. Use actual segment intervals if words are unavailable, recording `timing_precision: segment`.

Record the chosen take/version and measured duration. Rebuild shot/caption timing after changing it. Any trimmed/retimed audio needs a matching transcript.

Narration has three modes. For new synthesized speech (`mode: tts`), require `provider: google_ai_studio_tts`, `execution: online`, `allow_local_generation: false`, `automatic_fallback: none`, `interface: auto`, and `billing_mode: free_only`; resolve API/browser and actual model/voice at submission. For preserved source speech, use `mode: source_audio`, `provider: source_media`, `execution: imported`, source/stream references and the actual EDL; clear unused cloud settings and skip TTS. For a source with no speech, use `mode: none` with no invented narration. Do not install speech-synthesis models, probe/start a local voice backend, or run editor TTS/auto-voice. Original recorded audio, speech recognition within authorized available tools, local rendering, and audio processing do not synthesize speech.

On resume preserve original audio/request files and approval without executing legacy voice instructions. Verified user-source recorded speech stays selected in source mode; it must not be rejected as local synthesis or relabelled Google TTS. For generated narration with local/unknown synthesis provenance, obtain online speech of approved wording or report unavailable access. Save new TTS settings only when TTS is actually requested, keep previous requests as history, and rebuild dependent timing/captions/SFX. Source substitutions or material cut/message changes require updated review; unchanged content does not need a replacement script.

## SFX cues and mixing

Read [sound-design.md](sound-design.md). Copy [sfx-cues.template.json](../assets/sfx-cues.template.json) to `09_edit/sfx-cues.json` during planning. The cue file is the authoritative SFX plan, timing, mix settings, and provenance record; `production.json.audio_design` records its overall state. Register acquired sounds in the manifest's existing `assets` array as `type: sfx`, using the same asset IDs and local paths as the cue file.

The cue-file `schema_version` is independent of the production manifest. Resolve its `style_profile`, script version/hash, selected narration path/hash, measured duration, and composition revision from actual project state. Planned cues have event anchors but null actual times/asset IDs. Before rendering, finalize measured cue intervals and settings, or mark optional unavailable cues `omitted` with a reason. A cue is not accepted media until its linked file decodes and its source/license record is usable.

After narration changes, mark `audio_design.status: needs_retime` and `timing_status: stale` in the cue file; update all dependent cues and the mixed master. After an animation edit, re-resolve affected event anchors. Preserve original TTS audio and use `09_edit/audio_mix.wav` (or the actually chosen format) as a separate mixed master when pre-mixing. Ensure composition playback does not add the same voice/SFX tracks again.

On older manifests without `audio_design`, add these fields only when sound design is needed, retaining accepted assets and script approval. `mode: none` records a user's no-SFX choice and requires no sound download. Keep stock sounds private when their terms prohibit source-file redistribution; provide rendered output and source receipts/re-download information for an external handoff.

## Shot and asset-plan JSON

`06_scene_assets.json` contains all ordered scenes, including motion graphics, internet B-roll, user source media, and optional imagegen fallback images. It is a local plan, not a provider import file. A writing-phase plan uses estimated timing, null actual-audio fields, and no invented word indexes or acquired source files. After approval and actual narration, fill measured timing and real selected assets. Example of the measured shape:

```json
{
  "schema_version": "1.4",
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
      "asset_route": "motion",
      "search_terms": [],
      "source_candidates": [],
      "fallback_reason": null,
      "imagegen_prompt": null,
      "reference_images": [],
      "asset_ids": [],
      "editing_bindings": [],
      "avoid": ["unreadable microtext", "unrelated scenery"],
      "transition_out": {"type": "crossfade", "duration_sec": 0.2}
    }
  ]
}
```

These values illustrate fields, not a real script/measurement. Fill actual project values. Use `visual_type: motion`, `image`, `video`, or `source` and `asset_route: motion`, `internet`, `user_source`, or `imagegen`. Word indexes are zero-based inclusive indexes in normalized words; omit them for provisional/segment-only timing. Match `voiceover_segment` to the approved script and selected audio. Internet shots record useful search terms and actual candidate/source choices; imagegen shots additionally require a genuine `fallback_reason` and exact `imagegen_prompt`. A prompt never requests a complete narrated/captioned Reel.

The example shows one explanatory shot, not a complete production plan. A complete plan must also include at least one qualifying B-roll scene per video as specified below. Use `role: broll` for that scene; for `visual_type: image`, fill `broll_treatment` with its actual planned camera/parallax movement. Other roles can identify explanation, presenter, or title shots without counting them as B-roll.

For each acquired B-roll shot, record `editing_bindings` as described in [editing-options.md](editing-options.md): real engine/stage, clip/sequence ID, asset/path or supported uploaded-media ID, trim, measured timeline interval, layer, framing, and movement. Remotion also records frame intervals. For a HyperFrames stage, retain its detailed `hyperframes` binding from [hyperframes-broll.md](hyperframes-broll.md), using the actual recorded project folder. Placement derives from the shot's measured `start_sec`/`end_sec`; map final offsets explicitly across handoffs. Bindings must match actual editor projects. Editing metadata does not alter the approved spoken script.

Internet selection follows the actual approved subject, action, setting, crop, duration, and people constraints. Use a supported free download from the source's actual asset page and retain rights/source evidence. Save numbered originals under `07_broll_assets/`. A source link without an acquired usable file is not finished B-roll.

For an imagegen fallback, build the per-scene prompt from `script-and-assets.md`: actual theme, approved narration segment, visual purpose, subject/action/setting, style-only tokens, and exclusions. Record why sourcing is insufficient. Do not reuse the catalog sample's demo theme or sample-generation prompt. Log a content/purpose/style review for each acquired/generated asset; mismatched subjects fail even if their visual style looks correct.

Final text, captions, metrics, and diagrams remain editable layers in the selected editor's source project. A combined pipeline retains each stage's editable source even when downstream stages import a rendered clip. Generated depictions and generic stock do not prove a factual event or claim. Illustrative numbers must be clearly illustrative or omitted; factual numbers link to research sources.

New manifests use neutral `files.shot_plan` and `files.broll_assets` paths and `asset_jobs` for optional generation state. On older projects, respect existing manifest paths and preserve accepted assets, approval, and receipts. Read `06_flow_prompts.json`, `07_flow_downloads/`, `flow_jobs`, `gemini_prompt`, `flow_prompt`, or `visual_type: flow` only as legacy data; none authorizes new Flow/Gemini visual submissions. Record the internet-first policy for new acquisitions instead of deleting or blindly resubmitting old work.

## Minimum B-roll per video

The user's default is at least **one B-roll scene in every finished video**, across all styles and rendering routes. Apply the minimum independently to each deliverable in a batch; B-roll in one output does not cover another. A later explicit user request can change this requirement; style selection, generation failure, unavailable quota, or a `motion` route does not change it.

A qualifying scene is a supporting visual tied to an exact narration segment, showing its relevant subject/action/context. Prefer licensed internet footage or appropriate user-provided media. An appropriate sourced photo, or a justified imagegen fallback image, can qualify with purposeful pan/zoom/parallax during editing. An image treatment should make the visual readable and useful, rather than add an imperceptible movement just to fill a count. Pure diagram/typography/card animation, catalog sample posters, presenter-only footage, prompt text, and unused downloads do not satisfy the minimum.

Set `broll_requirement.min_scenes_per_video: 1`. During planning, identify at least one `role: broll` shot with an asset route and appropriate treatment. During production, acquire/review its real asset after script approval and insert it in the final composition. Use sufficient screen time for the action or idea; roughly 2-5 seconds is a starting suggestion, not an imposed minimum duration.

Before completing a video, inspect that interval in the actual final encode. Record qualifying scene IDs in `accepted_scene_ids` and an evidence entry for each output containing `video_path`, `scene_id`, `asset_id`, `clip_id`, `start_sec`, `end_sec`, review notes, and any actual frame/evidence path. Mark `review_status: passed` only when at least one qualifying scene visibly appears and explains the corresponding speech. A planned `role` or accepted source file alone is insufficient. Keep the requirement pending/failed when its visual review is unavailable or unsuccessful.

If internet sourcing cannot meet a required scene, use an appropriate still or a justified imagegen fallback within the approved scene's meaning. A source-specific factual shot cannot be replaced by fabricated evidence. Diagrams/cards cannot replace the last required B-roll. If the minimum remains unmet, report the specific production blocker and keep `stage` incomplete. On resume, add this requirement and the internet-first policy to older unfinished projects while preserving the approved spoken script; adding a relevant visual under the approved message does not require inventing new narration or approval.

## Checks before rendering

- Parse JSON using a real parser, such as `python -m json.tool`.
- Verify direct script approval and matching current/approved versions and hashes. Theme/style choices alone are insufficient.
- Verify actual user editor selection, supported selected-engine dependencies/handoffs, and exactly one final assembler. Verify speech provenance by mode: exact user-source audio/EDL for `source_audio`, actual Google AI Studio provenance for `tts`, or no synthesized narration for `none`. A recording is not local TTS; locally synthesized/unknown generated speech cannot be relabelled online. Missing cloud access never authorizes local synthesis and never blocks source-only audio editing.
- In source mode verify source IDs/hashes, selected passages/streams, approved cuts, output transcript timing, coordinated information/subtitle/motion layers and preserved face/action/meaning. Confirm source and intended output paths before render. New factual overlays have source evidence and are distinct from verbatim subtitles.
- IDs/order numbers are unique. Used asset IDs resolve to usable local files. Internet assets have recorded source/license evidence, and any imagegen fallback has a genuine recorded reason; source links or prompts alone are not produced footage.
- Each output has at least one planned and acquired qualifying B-roll scene bound to a real clip/sequence in the selected editor pipeline. Track/layer, trim, duration, framing, image movement, and caption/audio routing follow `editing-options.md`, plus `hyperframes-broll.md` for HyperFrames stages. After rendering, confirm its final visible interval and record evidence before marking that output completed.
- All intervals have end > start >= 0 and fit selected narration plus a deliberate short tail. Cover the last spoken word. Model transition overlap explicitly with separate tracks where HyperFrames requires it.
- Captions use the final timing, one visible group at once, with no stale group after its end.
- SFX anchors resolve to the current selected narration/animation; used files are accepted and have recorded source/license information. Optional omissions are explicit, required effects are present, and mixed-master/direct-track routing does not duplicate audio.
- Composition dimensions/fps and actual export agree. Duration follows measured narration and deliberate ending, not a provisional 35-second estimate.

## Review receipts

`11_final/VERIFY.md` records actual commands/results, inspected timestamps/frames, audio review, and fixes. Distinguish measured properties, frame review, and unavailable checks. Note the selected reference profile and timestamped examples showing visuals explain the speech.

When available, loudness tooling can target true peak <= -1 dBTP and approximately -14 to -16 LUFS; these are project mix targets, not asserted platform requirements. Review intelligibility, background ducking, joins, and all SFX event attacks/tails against the final encode. Record audible relevance/sync, mix routing, and any omitted cues. Do not claim listening checks based only on transcripts/metadata.

Deliver the encoded MP4, actual transcript/captions, ordered prompts, selected engines' editable projects and handoff notes, and truthful verification. Installed skills alone do not prove runtime, quota, login, browser access, editor tools, or online voices are ready.
