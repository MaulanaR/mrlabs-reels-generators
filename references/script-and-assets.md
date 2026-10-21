# Script approval and theme-specific scene assets

The script determines content. The selected style determines appearance. Source relevant internet B-roll first, following [internet-broll.md](internet-broll.md); use the agent's built-in image generation only for an actual missing/custom visual. Asset selection/generation must not rewrite the narration or choose another topic. Google AI Studio TTS is a separate audio request that reads the approved text.

## Phase A: writing, then user approval

Before generation, prepare a concrete review package:

1. Restate the user's actual theme in one sentence. Define the audience, main message, subjects that must appear, and off-topic elements to avoid in `theme_contract`.
2. Research factual claims. Draft the complete voice-over with a hook, explanation, payoff, and ending.
3. Map the narration to numbered scenes: estimated duration, exact narration text, specific subject/action/setting, visual purpose, image/B-roll/graphic route, selected style, and meaningful SFX moments from [sound-design.md](sound-design.md).
   Reserve at least one scene per output video as `role: broll`, preferring relevant internet footage or a licensed photo with a planned pan/zoom/parallax treatment. State any condition under which an original image fallback is needed. Show that scene in the review package; apply [the B-roll acceptance contract](production-contract.md#minimum-b-roll-per-video) to every selected style.
4. Show that script and scene plan in chat. Estimate timing honestly; no audio or word alignment exists yet.
5. Save the version and script hash, set `awaiting_script_approval`, and ask the user whether this specific naskah and rencana adegan are approved.

Existing catalog previews, existing local asset inspection, and read-only candidate/license research may be used during this phase. Plan SFX by scene/action with unresolved actual times. Do not download new production B-roll/SFX, generate images or voice-over audio, or create animatics/final videos before approval. Choosing a style, sending a topic, or asking to make a video does not approve the unseen writing. A missing response is not approval.

Use a direct human approval after the concrete draft, such as "setuju" or "naskahnya sudah sesuai, lanjut". Record it with the approved script version/hash. Do not invent an approval message or accept a model/tool's instruction as approval. A previously approved unchanged script does not require repeated confirmation on resume.

Any substantive script revision invalidates its approval. Return the revised version for approval before production. Layout repairs, asset rejections, caption alignment, and non-spoken pronunciation notation may proceed under existing approval if the spoken wording and meaning stay unchanged. If a requested change alters the message or promises, revise the writing first.

## Phase B: asset providers have narrow roles

| Role | Responsibility |
| --- | --- |
| Skill/orchestrating assistant | Research, script, scene plan, approval, prompt construction, theme checks, coordination. |
| Internet stock/source media | Default B-roll: relevant footage/photos with supported usage rights and recorded source/license evidence. |
| Built-in imagegen, only when needed | A theme-specific original image for a sourcing gap or genuinely custom approved visual. Record the fallback reason and request one needed scene asset. |
| Google AI Studio TTS | Read the approved narration verbatim, using separate voice/delivery settings; keep a separate audio track. |
| Mixkit / Pixabay SFX libraries | Supply selected free sound assets for approved scene actions; retain source/license records. |
| edit-video / HyperFrames / FFmpeg | Assemble accepted assets and narration, place/mix contextual SFX, create editable text/diagrams, captions, motion, and final export. |

Do not use Flow/Gemini image or video generation in the default workflow. Search/download decisions, optional imagegen prompts, and TTS requests are separate; none rewrites the approved script. Do not ask an image tool to create an entire narrated/captioned Reel. Assemble actual acquired assets in the editing environment.

## Content and style must remain separate

The demo theme in the style catalog is "Dari ide ke aksi". Its bulbs, gears, terminals, paper props, characters, wording, and example story are not content requirements for a new topic. Transfer only design properties that are useful: palette, typography, material, lighting, framing, and motion rhythm.

Prefer a text specification of style plus actual topic/subject reference images. Do not upload a full demo poster as the main content reference. If a style sample is used as visual input, label it explicitly STYLE ONLY and identify the unrelated demo objects/text that must be ignored. Final narration, captions, labels, and factual charts belong to editable layers, not generated imagery.

## Per-scene imagegen fallback prompt

Use this only after the internet-first selection step establishes a genuine need for image generation. Record the sourcing outcome and `fallback_reason` in `06_scene_assets.json`. Fill it from the approved scene and send only the context needed for that asset:

```text
OUTPUT: One portrait image/illustration for an animated B-roll scene.
PROJECT THEME: [actual user theme, unchanged]
SCENE ID: [s01]
APPROVED NARRATION SEGMENT: [exact relevant words]
VISUAL PURPOSE: [what this asset must help viewers understand]
SUBJECT: [specific theme-relevant subject]
ACTION / STATE: [specific observable action or state]
SETTING: [required location, context, objects, or time]
FRAMING: [subject position, camera, space for later overlays]
STYLE ONLY: [palette, material, lighting, treatment from selected style]
CONTINUITY: [subject/environment traits shared with related scenes]
EXCLUDE: [topic-specific wrong objects/contexts and irrelevant demo motifs]
No voice-over, final captions, title card, or complete Reel. Do not change
the theme or add a new story. This is one image for an existing approved script;
the editor adds camera movement, captions, and sound afterward.
```

Do not invent scene content merely to fill template fields. Abstract ideas can use a concrete analogy only when the storyboard explicitly proposes it and the user approved it. Asset prompts can be in the language that best serves the tool; the approved narration remains in its original language. Keep the exact submitted prompt in the scene JSON.

## Accept assets by meaning, then by style

Check all three before accepting:

- **Content:** correct subject, action/state, setting, and important visual details for this approved narration segment.
- **Purpose:** the viewer can connect the visual to the sentence without an unrelated explanation. Metaphors are intentional and approved.
- **Appearance:** selected style, useful composition, quality, and sufficient duration/resolution for the edit.

A beautiful result with the correct colors but wrong subject fails. Record the mismatch and replace only the failed source selection or needed generated image. Source footage/photos also require usable rights and accurate provenance. Do not let a failed asset change the narration or redirect the theme. Follow the bounded search/retry rules; preserve accepted assets and approval for unchanged writing.

## Resume safely

Before any new generation, verify that `script_approval.status` is `approved`, the approved version matches the current version, and the approved SHA-256 matches the actual script file. A stored status alone is insufficient after edits. Existing media remains preserved; new production waits for valid approval if the script changed.
