---
name: mrlabs-reels-generator
description: Draft a theme-specific Reel script and storyboard for user approval, then produce online Google AI Studio TTS narration, internet B-roll, free SFX, and an edit using the user's choice of Higgsfield, HyperFrames, Remotion, or a combination. Require at least one B-roll scene per video; use built-in image generation only when needed. Use for Reels, Shorts, explainers, and short product videos with an illustrated style catalog.
metadata:
  short-description: Approve the script, then produce a themed Reel
---

# MRLabs Reels Generator

Turn the user's theme into a researched script and storyboard first. Present them and wait for the user's explicit approval before generating any production media. After approval, continue through narration, scene assets, editing, and verified export. The default look is an editorial motion explainer with clear diagrams, typography, progressive reveals, and concise captions.

**Required order: theme -> research -> script/storyboard -> user approval -> narration and scene assets -> edit -> review/export.** Providing a theme, choosing a style, or requesting a Reel does not approve an unseen script. Never self-approve or treat a tool/model response as user approval.

**Online narration only.** Generate new speech exclusively with Google AI Studio TTS. Never install, start, probe, or invoke a local voice backend, local speech model, VoiceStudio, Kokoro, Piper, or a local TTS command. This restriction applies to companion skills, editor presets, resumed projects, and fallback/error recovery. Editors import the approved online narration; their TTS/auto-voice features stay off. Local audio files, FFmpeg conversion/mixing, and local video rendering are allowed; they do not synthesize speech. Missing cloud access/quota is a narration blocker, never permission for local synthesis.

**Every finished video must contain at least one relevant B-roll scene.** This applies independently to every Reel/Short in a batch and across all 15 styles. Find suitable footage on the internet first, using free assets with supported usage rights; an appropriate sourced image animated with purposeful pan/zoom can also qualify. Use built-in image generation only when a matching usable asset is unavailable or the approved scene needs an original visual. Plan B-roll in the storyboard, acquire it after script approval, and verify that it appears in the final edit. A caption card, diagram, style-preview poster, prompt, or unused asset cannot qualify. See [the B-roll acceptance contract](references/production-contract.md#minimum-b-roll-per-video).

Read [the illustrated style catalog](references/style-catalog.md) on invocation. Its [registry](references/style-catalog.json) contains 15 numbered styles and local example images: five derived from the user's references and ten original additions. Read [the reference analysis](references/visual-direction.md) for the original five videos and shared pacing/layout rules; do not download them again for every project. Read [the production contract](references/production-contract.md) when creating prompts, timing, or resumable state.

Use [watch](../watch/SKILL.md) for reference/output inspection and [Google AI Studio TTS](references/google-ai-studio-tts.md) for narration. Read [editor selection and handoffs](references/editing-options.md) before planning the edit. Load the installed Higgsfield, HyperFrames, or Remotion guidance only for the engines the user selects. `edit-video` is optional source-preparation guidance; it must not choose the editor or override the online-only narration rule.

Read [script approval and scene-asset prompting](references/script-and-assets.md) and [internet-first B-roll sourcing](references/internet-broll.md) before selecting or generating scene assets. The skill controls research, script, storyboard, and asset selection; Google AI Studio TTS reads the approved narration; the selected editor pipeline creates the finished Reel. Use online stock/source footage or photos first, respecting the actual scene and usage rights. Invoke the available `imagegen` skill and built-in `image_gen` tool only for a justified image fallback. Flow and Gemini image/video generation are not part of the default production path. Keep speech requests and visual asset work separate.

Read [sound design and free SFX](references/sound-design.md) when planning the storyboard and again when placing/mixing audio. Plan cues before approval; acquire production SFX after approval. Use Mixkit first and Pixabay as a fallback, choosing effects by the actual scene action and selected style. Use a lightweight local audio mix rather than installing a generative SFX model.

## Dependencies and workspace setup

This repository packages the orchestration skill, style previews, templates, and approval checker. It does not bundle the Watch engine, editor runtimes/plugins, or Google AI Studio sessions. Follow [README.md](README.md) for installation. Resolve skills by installed name and actual location, including plugin-qualified `app-6a3293e129088191abf0875820e839da:higgsfield` and `hyperframes:hyperframes`; do not hardcode a user's plugin cache/version. Remotion may use an existing supported runtime and official documentation when no companion skill is installed. Require only the selected engines' dependencies. Internet asset search/download needs available web/browser tools. The optional image fallback needs an available built-in image-generation tool; do not install a local model or silently switch to an external API when it is unavailable.

If the selected route uses Herk Edit Kit resources, use `HERK_EDIT_KIT_ROOT` when configured; otherwise inspect the installed companion skills' setup notes or an existing workspace checkout. Verify the resolved directory contains the expected `AGENTS.md`, `package.json`, and required utility files, then read its guide. Record the resolved location in the local project's notes. Missing editor dependencies do not prevent script/storyboard drafting; explain any setup blocker before production. Never run a setup step that installs a local voice model.

## 1. Get the theme

Always present visual examples as described in the style catalog, using Markdown image embeds with absolute local paths. A plain filename or link alone is not an inline image.

If no theme is supplied, show the three catalog boards (01-05, 06-10, 11-15) and the interactive gallery link, then ask: “Tema Reels apa yang ingin dibuat? Nomor gaya boleh disebutkan juga.” The theme is required; selecting a style is optional. Do not start research/generation before the theme is known.

If the theme and a style are supplied, resolve its number/name/ID, display that example PNG, and proceed to script drafting. If only a theme is supplied, show up to three relevant example images, state the automatic choice, and draft without requiring another style selection. A request to browse styles should show the gallery rather than begin production.

When a theme is provided, begin research/planning. Record the actual subject, main message, required subjects/actions, and things to avoid in the theme contract. Infer mood, canvas, palette, and visual route from the selected style; the style must not change the topic. Default to Indonesian, 1080 x 1920, 30 fps, approximately 30-40 seconds, one takeaway, and an original script. User-specified details override defaults. Record the resolved style ID/number and preview path in production.json.

Before approval, research, show existing style previews, write the full spoken script, and propose the storyboard/B-roll and SFX plan. Existing local assets may be inspected and public candidate/license pages researched; wait until approval to download new production B-roll/SFX, generate images or TTS audio, or create animatics/video renders. Present the concrete script for approval and wait. After approval of that version, proceed with production without repeating the same approval request.

User approval of the presented script/storyboard authorizes its planned production within the existing allowance/budget. It does not authorize purchases, publishing, or an unapproved cloud/paid voice provider. Preserve explicit limits. A substantive script change requires a revised script and fresh approval; technical timing/layout repairs within the approved script do not.

### Choose the editing engine

Offer **Higgsfield**, **HyperFrames**, **Remotion**, or **Gabungan** using [editing-options.md](references/editing-options.md). Accept one engine, any explicit pair, or all three. Reuse a choice already stated by the user; a style number or `render_route: motion/hybrid` is not an editor choice. If unspecified, ask once: "Untuk editing, pilih Higgsfield, HyperFrames, Remotion, atau gabungan? Kalau gabungan, sebutkan tools yang ingin dipakai, atau pilih semuanya."

Continue independent research/script drafting while that choice is pending, and include the unresolved choice with the script review. Do not start production until both the actual script is approved and the editor choice is recorded. Do not silently default to HyperFrames. For a combination, propose each engine's job and one final assembler in the review package; ask only about decisions that materially affect the output or cost. Merely updating/browsing this skill does not open an editor.

## 2. Research and reference images

Research factual themes using current, preferably primary sources. Save claim-to-source links and access dates. For fiction, identify the story as fictional and research only context that needs accuracy. The reference videos' prices, star counts, example commands, promotional claims, and auto-captions are not verified sources for a new Reel.

Find several relevant image references and record source/rights information. Use unknown-license images for research, not final artwork. Prefer accurate screenshots or editable HTML/SVG for UI, code, diagrams, and charts. Never treat generated imagery as evidence for facts.

For new video references, use `$watch`, inspect every retained frame plus the transcript, and save index IDs. Sample additional cached timestamps if deduplication hides important changes. Use ask/search for follow-ups on indexed videos. Do not download private/access-controlled content or evade site restrictions.

Choose a route per shot:

- **Motion graphics:** diagrams, comparisons, numbered workflows, UI cards, code, labels, statistics, or explanatory illustrations. Build accurate editable layers in the selected editor pipeline.
- **Internet B-roll (default):** relevant object/action shots, places, environments, or photos from free online sources with supported usage rights. Prefer suitable real footage; animate stills when that serves the approved scene.
- **Imagegen fallback:** a scene-specific original image only when sourcing cannot meet the approved scene or original imagery is necessary. Record the reason and animate the accepted image in the selected editor.
- **Source/presenter:** user-provided footage, authorized screenshots, or supplied brand assets. A presenter is optional for theme-only production.

The common reference pattern is motion-led explanation. Keep that direction while reserving at least one scene for relevant internet B-roll or a justified image fallback. A catalog route named `motion` means motion-led with this B-roll insertion, not an exemption from the minimum. Style selection does not authorize an external video-generation service. Build final captions, UI labels, repository metadata, and factual charts as accurate editable layers.

Style samples use a demonstration theme, "Dari ide ke aksi". Transfer only palette, typography, lighting, layout, and motion grammar. Do not carry their lightbulbs, gears, terminals, characters, demo text, or subject matter into another theme unless that scene's approved script calls for them. Prefer theme-specific content references and a text style specification when an image fallback is needed.

## 3. Prepare the project and numbered drafts

Create a dedicated project folder `reels-projects/<theme-slug>/` in the user's workspace. Reuse it when continuing the same Reel. Preserve sources/intermediates. Copy [the manifest template](assets/production.template.json) to `production.json`; save decisions and observed state after each stage or external generation. Use ordered names so clips and prompts stay aligned:

```text
reels-projects/<theme-slug>/
  production.json
  DESIGN.md
  01_research.md
  02_visual-references/
  03_storyboard.md
  04_voiceover_transcript.md
  05_tts_request.json
  06_scene_assets.json
  07_broll_assets/
  08_voiceover/
  09_edit/
    sfx-cues.json
    sfx/
  10_editing/
    higgsfield/   (only if selected)
    hyperframes/  (only if selected)
    remotion/     (only if selected)
    handoffs/     (for a combined route)
  11_final/
```

Write a hook, explanation/mechanism, concrete example/payoff, and concise closing. Start with a recognizable problem, curiosity, or specific promise; remove generic introductions. Usually plan 4-7 main beats, each with one core message, exact narration segment, and a visual action that explains it. Use a CTA when it serves the Reel. Do not invent a discount, URL, or pinned comment.

Mark at least one shot `role: broll`, with its exact approved narration segment, subject/action/setting, asset route, and planned treatment. Give it enough screen time to explain the line (roughly 2-5 seconds is a useful starting point, not a fixed limit). For an image-based B-roll scene, specify the purposeful pan/zoom or parallax treatment. Include that scene visibly in the storyboard presented for approval.

Start around 150-185 words/minute for Indonesian, then judge actual delivery; the references range approximately 125-200. Provisional storyboard timings are replaced by measured audio timings. Use progressive reveals and a recurring motif rather than repeating the same card layout or unrelated footage for every sentence.

Create `DESIGN.md` now, before visual prompts or composition HTML, from the selected profile and theme: colors/roles, fonts, hierarchy, background, caption position, motion/transitions, and anti-patterns. The supplied references authorize this direction; infer missing design choices and record them instead of asking for a new style selection. Honor explicit brand requirements.

Include a sound direction in `DESIGN.md` using the selected style's profile from `sound-design.md`. Copy [the SFX cue template](assets/sfx-cues.template.json) to `09_edit/sfx-cues.json` and plan only useful accents, transitions, foley, or ambience. Start with roughly 4-8 discrete accents for 30-40 seconds as a sparse design suggestion, not a quota. Give every cue a scene/action, purpose, and event anchor; leave actual times and asset IDs null until measured and acquired. Honor requests for fewer effects, no SFX, or an existing supplied sound pack.

`06_scene_assets.json` follows the production contract: ordered shot IDs, actual audio anchors, start/end times, narration, core message, visual route/action, sourcing queries/candidates, any justified `imagegen_prompt`, reference images, and asset mapping. Motion-only shots need no stock download or generation prompt. Save actual source/license records and numbered files such as `01_s01_hook_take01.mp4` or `01_s01_hook_take01.png`. Use legacy plan paths from an existing manifest when resuming rather than discarding earlier work.

Start with a provisional plan here using estimated timing; do not invent word timestamps before audio exists. Finalize measured timings/anchors after approved narration in step 5 and before submitting assets in step 6.

Retain rejected takes with their status. Record accepted files, submission attempts, and observed remote job/project identifiers in the manifest. On resume, inspect files and pending jobs before submitting anything again. Do not regenerate accepted assets merely because the previous turn stopped waiting.

## 4. Present the script and wait for approval

Show the full narration, numbered scenes with estimated duration, each scene's visual/B-roll idea and intended SFX moments, selected style, editor choice (or pending options), combined-stage responsibilities when applicable, and any factual caveat. The user must be able to review the actual proposed content in chat; a file path alone is insufficient. Save the script/storyboard version and current script SHA-256, set `stage: awaiting_script_approval` and `script_approval.status: pending`, then ask: "Apakah naskah dan rencana adegan ini sudah sesuai? Jika setuju, saya lanjut membuat voice-over Google AI Studio TTS, gambar/B-roll, menyiapkan SFX, dan videonya menggunakan editor pilihan Anda."

Wait for a direct user response. "Setuju", "naskahnya sudah sesuai, lanjut", or equivalent approval after the draft is shown applies to that displayed version. A style selection, silence, initial theme request, or generated model text does not. Revisions remain in the writing phase until the revised script is approved. On approval, record its version/hash and the user's approval text before starting step 5. On resume, reuse valid prior approval for the unchanged script; missing/stale approval blocks production.

## 5. Generate narration with Google AI Studio TTS after approval

Check the current script matches the approved version/hash before any generation. This gate also applies to existing jobs and resumed projects; do not submit new work against a changed, unapproved script.

Run `python <skill-directory>/scripts/check-script-approval.py <project-directory>` before producing narration, downloading production B-roll/SFX, generating an image, or rendering (also on resume). A nonzero exit stops production and returns to script review. The checker is read-only: record only real human approval, then run it; it does not grant approval itself.

Also check `editing.selection_status: selected`, the user's actual choice, planned engine availability, and the online-only narration policy. The script checker checks script approval only; it does not validate editor selection or narration provenance. An old manifest or companion workflow cannot grant permission for local synthesis.

Read [Google AI Studio TTS](references/google-ai-studio-tts.md). Use the Gemini speech-generation API when an authorized key and confirmed free-tier access are available; otherwise use the user's signed-in Google AI Studio speech interface through available browser control. Select a currently supported TTS model and prebuilt voice, record them, and keep one voice consistent across the Reel. Set `execution: online`, `allow_local_generation: false`, and `automatic_fallback: none`. Never use an editor's voice feature as a replacement.

Save the approved spoken text, separate non-spoken delivery instructions, selected model/voice, interface, script version/hash, and exact submitted settings in `05_tts_request.json`. Ask TTS to read that text verbatim in Indonesian by default. Download/decode the actual result to `08_voiceover/`, probe the audio, and review wording, pronunciation, pace, pauses, and ending. Use the response MIME type and encoding; never assume every result is raw PCM or contains word timestamps.

Use free access only by default. If free quota or account access is unavailable, record the blocker and preserve the project; do not enable billing, submit paid requests, or switch providers automatically. Keep API keys in the configured environment/secret store, outside prompts, logs, and project JSON. Ask for login or secure key setup only when needed to proceed.

**The actual final voice track controls the timeline.** Obtain word or segment timing through an available transcription/alignment tool or genuine per-segment audio boundaries described in the TTS reference. Do not assume TTS returns alignment. Keep normalized timings beside the audio. Never spread words evenly across an estimated duration. If word timing is unavailable, use genuine segment timing and segment captions instead of fake karaoke timing.

If narration does not fit, first adjust visual timing within the approved script and preserve natural delivery. If the spoken script needs rewriting, return the revision for approval before regenerating. Keep the approved script file unchanged; put non-spoken pronunciation markup or timing splits in TTS/timing metadata so approval remains valid when the spoken wording/meaning is unchanged. Rebuild shot timing/captions after voice edits; never use stale timestamps.

## 6. Source approved B-roll from the internet first

Check valid script approval first. Follow `internet-broll.md`: select footage/photos for the exact approved narration segment and theme contract, starting with Pexels/Pixabay or suitable existing user assets. Inspect the actual asset page and license, download only selected files to `07_broll_assets/`, and record source/rights and measured media properties. A search thumbnail or a download link alone is not an accepted asset.

Stop searching once a suitable usable asset is found. If no candidate fits after a focused search, or the approved scene genuinely needs an original illustration, record `fallback_reason` in the scene plan and use the built-in image-generation path after reading `imagegen`. Generate only the needed scene image, not a complete Reel, and copy its returned local output into `07_broll_assets/` before composition. Keep exact submitted prompts in `06_scene_assets.json`; image requests must not rewrite the approved narration or invent a new theme.

Before accepting an asset, compare subject, action, setting, people restrictions, crop/readability, and rights with that approved scene. A matching palette alone is not sufficient. Reject unrelated attractive imagery, repair only the failed selection/prompt, and retain approval for unchanged narration. Follow the concrete prompt and acceptance rules in `script-and-assets.md`.

Use relevant footage directly with deliberate trim/crop, or animate a still using purposeful pan/zoom/parallax. Final text, diagrams, and captions remain editable HyperFrames layers. Mute embedded speech/music unless deliberately selected for the mix. Do not open Flow/Gemini to create video or images as an automatic sourcing fallback.

Record asset state and reuse accepted files on resume. Inspect an existing image-generation result before retrying; allow at most two additional attempts for a failed needed image. If sourcing and the permitted image fallback cannot supply the required B-roll, preserve the project and report the blocker. A diagram/card replacement does not fulfill the minimum.

Do not bypass login, CAPTCHA, access controls, or browser security. Ask only for necessary user interaction, unavailable browser control, exhausted required quota, or an unapproved purchase. Save state first and continue other independent assets while external jobs run. Do not claim download success without a usable local file.

### Acquire the approved SFX plan

Run the script-approval check before acquiring new SFX. Follow `sound-design.md`: reuse suitable existing files with known rights; otherwise inspect the actual free asset page, download only relevant selections from Mixkit/Pixabay, and record provenance/license information and measured audio properties in the cue file. Save numbered originals under `09_edit/sfx/` and register their asset IDs in the manifest. A search result, preview URL, or cue plan is not a downloaded effect.

Choose exact cues after the final narration and visual beats are known. If no suitable free asset is accessible, omit an optional cue and record why; an explicitly required sound remains a blocker. Do not purchase assets, subscribe, or substitute an unrelated sound to fill a target count. Preserve accepted downloads on resume.

## 7. Assemble footage and narration

Follow [editing-options.md](references/editing-options.md) for the recorded engine(s). Preserve originals, probe accepted assets, and assemble with the approved online narration as a separate controlled audio track. Use FFmpeg or the selected editor's supported media preparation. Load `edit-video` only when its source-footage preparation is useful, applying its preservation/sync guidance without invoking voice generation or overriding the user's editor. Do not run talking-head silence/mistake processing when no such source speech exists.

Read the project's existing `DESIGN.md` before composing; use the same identity established for the shot plan and generated assets.

Bind every B-roll shot to an actual editor clip/sequence with measured timing, source trim, portrait crop, and visual layer. Record editor-specific bindings in the shot plan. If HyperFrames is selected, also read [HyperFrames B-roll integration](references/hyperframes-broll.md). For a combined route, export and probe each accepted handoff before importing it into the next stage. A download, import, or project link alone does not prove the asset appears in the final edit.

## 8. Add captions, B-roll, effects, and render

Use only the selected routes in [editing-options.md](references/editing-options.md): Higgsfield Video Editor/Katana through its resolved `/use-video-editor` handoff; HyperFrames through its installed composition/CLI skills; Remotion through its installed guidance or the supported runtime and official docs. In a combined route, run the planned stages in order and render the master with the recorded final assembler. Do not run all editors just because they are available.

For HyperFrames stages, read the installed `hyperframes`/`hyperframes-cli` skills plus captions, typography, motion, and transitions references; follow `hyperframes-broll.md`. Use `editing.project_paths.hyperframes` (new default `10_editing/hyperframes/`), respecting an existing `10_hyperframes/` project on resume. Keep video muted with `playsinline` and the approved narration/mixed master as separate audio. Skip all TTS commands, local voice references, and auto-voice setup in editor/kit guides.

Create a lightweight animatic in the chosen pipeline with measured narration and planned graphics, inspect it internally, and continue to finishing. Add meaningful motion, accepted B-roll, transitions, and actual-audio captions using the selected engines' supported features. Prefer short phrase groups, one visible group, and selective keyword emphasis. Keep hero text/captions from competing. Use the profile's portrait safe-area guidance. Preserve one narration clock across engines; choose one owner for final captions and one owner for the final audio mix.

Resolve `09_edit/sfx-cues.json` against the selected narration take and actual animation events, aligning each sound's audible attack with its intended action. Use measured timing, deliberate gain, trims, and short fades. Re-resolve dependent cues after narration or animation changes. Place voice, SFX, and any optional music on separate controlled tracks, prioritizing narration and ducking overlapping background sound when needed. Mix through the selected final editor's supported audio path or FFmpeg and include each sound once; keep a mixed master separate from the original TTS file. Follow `sound-design.md` for cue fields, style choices, and mix review. Remove duplicate audio and avoid unrelated filler footage.

Run applicable checks for the actual engine: HyperFrames preflight/lint/validate/inspect, Remotion's configured project checks and composition preview, or Higgsfield's supported editor/job review. Do not demand HyperFrames checks on a Remotion-only/Higgsfield-only edit. Render and inspect hero frames, every scene boundary, captions, first/last seconds, and audio joins. A successful check/render is not a visual pass.

Use `$watch` on the encoded draft for visual/narrative review; inspect frames yourself when no vision-provider description is available. Save timestamped issues, fix the responsible layer, and re-render that stage. Two focused review passes are a useful default; unresolved failures remain explicit rather than being labelled finished.

Acceptance requires a clear opening within roughly two seconds, delivery of the promised takeaway, visuals that explain speech, accurate readable labels/claims, consistent identity, synced captions without collisions, an intact closing, and no unintended blank frames, clipped audio/words, damaged media, or duplicate voice tracks. Review every SFX cue for scene relevance, event sync, intelligible narration, clicks, abrupt tails, and duplicate playback. Check encoded dimensions/duration/streams and actual A/V sync.

For each final video, inspect the qualifying B-roll interval in the actual encode and record scene ID, asset ID, composition clip ID, final timecodes, and visual review evidence in `production.json.broll_requirement` and `VERIFY.md`. Review its entry, middle, exit, and both scene boundaries for actual video movement/image treatment, correct crop, caption visibility, and continuous narration. At least one accepted, visible, theme-relevant B-roll scene is required before `stage: completed`; a storyboard flag alone does not satisfy this check.

## 9. Deliver and report

Export `11_final/<slug>_final.mp4`, default H.264/AAC, 1080 x 1920, 30 fps. Keep the editable composition, voiceover, transcript/captions, storyboard, ordered JSON, SFX cues/source receipts, research/source notes, and downloaded originals in the user's local project. For an external editable handoff, follow each asset's redistribution terms; restricted stock SFX stays out of a distributed source bundle. Write `11_final/VERIFY.md` with commands/results, actual inspected timestamps, SFX/mix review, and limitations. Never claim a check that was unavailable or not performed.

Record the final path and `stage: completed` only after acceptance. Deliver exact usable paths. Upload or publish only when separately requested.
