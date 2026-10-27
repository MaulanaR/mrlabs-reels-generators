---
name: mrlabs-islamic-content
description: Create researched Islamic videos from a theme, or optionally edit supplied footage, with verified Quran/hadith references, no human or animal faces, no music, Google AI Studio narration, smooth 3D-priority HyperFrames motion, and contextual internet B-roll. Present the script, sources, storyboard and Instagram credits for approval before production. Use for Islamic education, reminders, prophetic history and daily-life reflections.
metadata:
  short-description: Konten Islami berdalil tanpa wajah dan musik
---

# MRLabs Islamic Content

Build a standalone Islamic-content project from the user's theme and Instagram username. Default to Indonesian narration of explanation/meaning, portrait 1080 x 1920 at 30 fps, and a duration that follows the approved discussion. HyperFrames is the required editing/motion route; use Three.js where real 3D geometry or camera movement is useful. There is no inherited 15-style catalog or editor-choice gate.

**Order:** theme + username -> religious research -> full script, sources and storyboard -> direct user approval -> Google narration and acquired assets -> HyperFrames -> encoded-output review -> export. Never treat a topic, style choice, silence, or tool response as approval.

## Non-negotiable content rules

- **No human or animal faces anywhere:** source footage, generated art, 3D meshes/textures, reflections, screens, photographs, statues, thumbnails, style previews, and transitions. Hands, backs and faceless silhouettes may appear when relevant. Inspect real results; a negative prompt or automated detector alone is not proof.
- **Prophets:** only an abstract light marker with the verified prophet's name in a separate editable text layer at its center. No prophet body, silhouette, face, portrait, avatar or impersonated voice. The marker is a narrative label, not a claim about physical appearance. Do not depict Allah.
- **Religion:** verify each religious assertion against Quran/tafsir or a traceable hadith and grading. Separate quotation, translation, tafsir and the narrator's explanation. Never invent prophetic dialogue, rewards, story details, unanimity, or declare a current disaster/personal misfortune divine punishment without evidence. Read [religious research](references/religious-research.md).
- **Quran:** Google narrates the Indonesian meaning/explanation, not AI tilawah. Optional Arabic display must be verified editable RTL text, with proper shaping/harakat; never generated image text. Symbolic imagery of unseen matters must not be presented as a literal reconstruction.
- **No music:** exclude music in stock audio, templates, source footage, melodic SFX, instrumental nasheed, hum/choir beds and tonal sequences. Use only contextual nonmusical SFX/ambience. Keep the voice intelligible.
- **Speech generation:** Google AI Studio TTS online only, with confirmed free access by default. No local TTS, voice-model installation, VoiceStudio, Kokoro, provider substitution, auto-voice editor features or automatic billing. Original user-recorded speech is not local synthesis and may be preserved in optional source mode when it meets this skill's policies.
- **Every complete video needs at least one actual relevant B-roll scene**, acquired from internet/user assets first, placed in the edit and reviewed in the final encode. A caption card, pure diagram, prompt or unused download is not B-roll. Imagegen is only for a documented sourcing gap/custom visual.
- **Credits:** use the actual supplied Instagram username, followed by `Like & share jika bermanfaat.` Do not infer a handle from old projects or attach invented religious promises to engagement.

## 1. Intake and project

Ask for a missing theme and Instagram username together. Do not request the API key until TTS is actually needed. If a username is missing, research/drafting can continue but approval/production/final credit cannot use a placeholder. Duration is optional; infer a natural length and show the estimate, without a fixed 35/60-second ceiling.

Read the [Islamic background catalog](references/style-catalog.md) and show its new board/gallery or up to three relevant local preview images using absolute-path Markdown image embeds. These are background/layout concepts, not religious evidence or a pre-rendered video. Choose the context automatically unless the user chooses one: azab, daylight desert, mosque, city, home, or river. Never inherit the original skill's styles or demonstration subjects.

Create `islamic-projects/<theme-slug>/` in the actual workspace and copy [production.template.json](assets/production.template.json). Resolve paths relative to that root. Keep originals/intermediates. Resolve installed `watch`, `hyperframes:hyperframes`/`hyperframes`, CLI, GSAP and imagegen guidance by their actual installed locations, not a hardcoded plugin cache version. Herk helpers are optional; resolve `HERK_EDIT_KIT_ROOT` only if needed and skip all speech-model setup.

```text
production.json
DESIGN.md
01_research.md
01_religious_references.json
02_visual-references/
03_storyboard.md
04_voiceover_transcript.md
05_review_package.json
05_tts_request.json          (only when new TTS is requested)
06_scene_assets.json
07_broll_assets/
08_voiceover/
09_edit/sfx-cues.json
10_editing/hyperframes/
11_final/
```

Optional original-video input selects `workflow_mode: source_video_edit` only when supplied explicitly for editing, not as style inspiration. Read [source-video-edit.md](references/source-video-edit.md). Preserve its exact identity/transcript/approved cuts; all no-face, religious-source, no-music and portrait rules still apply. Do not silently preserve prohibited faces/music or replace the source with an unrelated video.

## 2. Research and writing

Prepare the actual religious claim/source ledger first; read [religious-research.md](references/religious-research.md). Use Quran Kemenag for Indonesian translation/tafsir, and hadith sources with collection, numbering/edition, grade and grading authority. Research current factual context separately. Unverified material remains excluded/pending, not a compelling invented hook.

Write a truthful hook, explanation, context, takeaway and respectful closing. Maintain nuance and the distinction between direct quotation and paraphrase. New narration is third-person explanation; do not act out or synthesize a prophet speaking. Preserve the approved spoken wording; non-spoken production notes stay separate.

Map each beat to actual narration, subject/action/setting, background, visual purpose, intended 3D movement, optional prophet light/name marker, B-roll placement, source reference and nonmusical SFX. For azab/warnings use dark restrained lighting/fog/space fitting the verified topic; everyday themes can use bright desert, mosque, building, home, river or another accurate location. Do not force every theme into a desert or invent unseen details for spectacle.

Create `DESIGN.md` before prompts/composition: palette, type hierarchy, scene materials/depth/camera, smooth motion/transitions, caption panel and safe areas, no-face/no-music constraints, prophet marker treatment and exact credit. [visual-direction.md](references/visual-direction.md) and [motion-3d.md](references/motion-3d.md) describe implementation choices.

Use a subtle caption border and about 24 px corner radius at 1080 px width, maximum two lines, strong contrast and actual audio timings. Keep Arabic quotations, Indonesian subtitles, source labels and main visuals distinct and legible. No fake word alignment or miniature source text.

## 3. Review package and approval

Show in chat the full narration, cited claims, numbered scenes with estimated duration, B-roll and SFX plan, prophet treatment if applicable, exact Instagram credit/CTA, and intended full-length output classification. A link alone is not review. Save these artifacts with actual script version/hash and pending approval.

The inherited `scripts/check-script-approval.py` still checks the script's real bytes/version and recorded human approval. Additionally freeze all review artifacts and the reviewed policy/credits using [the production contract](references/production-contract.md). Run `python <skill>/scripts/workflow_guard.py <project> --digest` to compute a read-only package hash; this never approves anything. On genuine human approval record the matching script approval and package hash. If a material reviewed artifact changes, request revised approval; purely technical fixes go in separate metadata without rewriting the approved package.

Before any TTS, new production asset/SFX download, image generation, animatic, editor import or render, run `python <skill>/scripts/workflow_guard.py <project>`. A nonzero exit blocks production. No fabricated approval, evidence or verified claim. Reuse unchanged valid approval on resume.

Before approval, inspection/acquisition of user-supplied input for analysis, factual research, source/license searches, existing assets, script/storyboard and design drafting are allowed. New production media and renders wait.

## 4. Voice, assets and sound

Read [google-ai-studio-tts.md](references/google-ai-studio-tts.md) only for new TTS. Load the key programmatically from the skill-local `.secrets/google-tts.env` first, then configured environment. Use `scripts/google_tts_credentials.py --status` for readiness only; it never prints the key. If absent, ask the user to create/fill the private file or a secret input, never paste the key into chat. Keys never enter prompts, JSON, logs or Git. Model/voice and quota are resolved at production time; current official API schemas must be followed.

Google reads the approved Indonesian meaning/explanation verbatim with separate delivery direction. Save/decode the actual returned audio, measure it, and review wording/pronunciation/endings. Use available genuine word alignment, otherwise actual measured sentence/segment boundaries and segment captions. No heavy local speech-model installation. Free quota/access failure preserves the project and blocks new TTS without switching providers or starting billing. Source-audio mode skips TTS setup and retimes the source via its approved EDL.

Read [internet-broll.md](references/internet-broll.md) and [script-and-assets.md](references/script-and-assets.md). Reuse authorized suitable assets; search Pexels/Pixabay or other rights-verifiable sources for the actual subject/action first. Record creator/title, real page/license, attribution, dates, file hash, media properties, chosen crop/trim and content/face review. Download selected files after approval into `07_broll_assets/`. Use imagegen only for a genuine gap, never for scripture text. Reuse accepted files on resume; inspect remote state before retrying generation.

Read [sound-design.md](references/sound-design.md) and copy [sfx-cues.template.json](assets/sfx-cues.template.json). Prefer wind/water/footsteps/doors/paper/material foley/thunder when context warrants. Audition assets; a filename/category does not prove absence of music. No music quotas, melodic risers/chimes or stock soundtrack. Silence is acceptable when no useful effect exists.

## 5. HyperFrames and 3D-priority edit

Read installed HyperFrames/CLI guidance, the relevant caption, typography, motion and transition references, plus [editing-options.md](references/editing-options.md), [motion-3d.md](references/motion-3d.md) and [hyperframes-broll.md](references/hyperframes-broll.md). This skill already selects HyperFrames; do not ask for Higgsfield/Remotion choice or activate them automatically. Skip editor TTS/music generation.

Use lightweight purposeful 3D first: geometry, scene depth, camera, lighting and parallax. Use actual Three.js for real geometry/camera when useful and supported; identify CSS depth as 2.5D. Verify WebGL capture and resource loading before depending on it. All movement must derive deterministically from composition time, using finite registered paused GSAP timelines; no independent wall-clock loop or random playback. Preserve smooth acceleration/deceleration, camera continuity and time to read. Captions stay a readable 2D overlay.

Place real B-roll with measured start/end, trim, crop, visible image movement where applicable, proper layers and separate audio. Keep video muted and use selected Google narration/source audio or one premixed master; no duplicate speech/SFX. Stage only usable local assets, not expiring preview URLs. Keep one caption owner and one final audio mix.

End with a legible roughly five-second credit (extend if needed), actual username and the approved CTA. Include the tail in actual duration/platform classification. Preserve discussion length even above three minutes; do not automatically truncate or split.

## 6. Review, export and delivery

Run supported HyperFrames lint/validate/inspect, preview hero frames, scene boundaries, prophet-name frames, faces/reflections/screens, Arabic/subtitle layout, B-roll intervals, closing and audio joins. Inspect the actual encode and listen for music, intelligibility, truncation and duplicate audio. `watch`/detectors can assist but do not prove absence of a face or music across an entire clip. Check source frames particularly during turns/camera movement/transitions; a missed face requires crop/replacement/removal and re-review.

Save actual evidence and limitations in `11_final/VERIFY.md`, `policy_review`, caption/motion/SFX review and B-roll evidence. Use `workflow_guard.py <project> --final` before completion; flags must reflect actual review, not simply be set to pass. A missing visual/listening check keeps the relevant acceptance pending.

Export full portrait H.264/AAC MP4, SRT/VTT (and actual word/segment timing), editable project, approved script/storyboard, religious-source ledger, research/asset-license receipts and truthful verification. Derive YouTube classification from measured final duration: up to 180 seconds is eligible by duration for Shorts; above it is a normal vertical video. Check current Instagram rules for the actual publishing route; if unavailable mark unverified and preserve the master. Do not claim overall platform eligibility from duration alone.

No upload/publish, new repository or GitHub push without a separately specified destination/authorization. Keep the parent skill and all credentials isolated.
