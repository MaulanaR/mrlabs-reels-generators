# Put B-roll into the HyperFrames edit

Read only when HyperFrames is a selected engine, before authoring composition HTML or inserting/replacing B-roll. This guide connects the approved shot plan to actual HyperFrames media elements. Follow [editor selection/handoffs](editing-options.md), the [minimum B-roll requirement](production-contract.md#minimum-b-roll-per-video), and [sound-design mix routing](sound-design.md#mix-and-review).

Use the installed [HyperFrames skill](../../hyperframes/SKILL.md) and its media/timeline contract, [transitions](../../hyperframes/references/transitions.md), and [caption guidance](../../hyperframes/references/captions.md). These links assume sibling skill folders; if HyperFrames is installed through a plugin or another supported skill root, resolve the corresponding files there instead. Read the project's `DESIGN.md` before HTML. Resolve concrete CLI options from the available version when producing a Reel. This skill update alone is not evidence that a composition has been rendered successfully.

## 1. Bind the approved shot to a real asset

After script approval and narration timing, select an accepted theme-specific clip or image for every B-roll shot. Follow [internet-first sourcing](internet-broll.md): use appropriate internet/user assets, and invoke imagegen only for a justified gap. Preserve actual downloads or accepted generated originals in `07_broll_assets/`. Use the exact `asset_id` from the manifest and stage required files inside the recorded HyperFrames project's `assets/`, for example under `video/`, `images/`, and `audio/`. New default: `10_editing/hyperframes/`; preserve an existing `10_hyperframes/` folder. Use local paths relative to the composition document; do not depend on a remote preview URL, an absolute Windows filesystem string in `src`, or a project-sibling path the composition server cannot serve.

Record a `hyperframes` object on the corresponding `06_scene_assets.json` shot (or the actual legacy plan path recorded in a resumed manifest):

| Field | Meaning |
| --- | --- |
| `clip_id` | Actual unique timed video/image element ID in HTML |
| `wrapper_id` | Actual non-timed framing/animation wrapper ID |
| `source_path` | Staged media path relative to the composition document |
| `media_start_sec` | Measured trim offset into source video; zero for an image |
| `track_index` | Actual media scheduling track, distinct from overlapping clips |
| `z_index` | Intended CSS visual layer, applied to the correct wrapper/stacking context |
| `layout` | Chosen `full_frame`, `inset`, or `picture_in_picture` treatment |
| `fit` | Actual `cover` or `contain` choice |
| `object_position` | Actual focal/crop position appropriate to the subject |

Derive timeline placement from the shot's measured `start_sec` and `end_sec`; these fields are the timing source of truth. For an animated image, also keep its intended pan/zoom/parallax in `broll_treatment`. Resolve bindings when real assets are known rather than inventing filenames or completed media during script planning.

## 2. Put media on the framework timeline

- Use a visible root composition with explicit ID, start, duration, dimensions, and a registered synchronous paused GSAP timeline. Root `index.html` is not hidden inside a template.
- For video B-roll, use a real `video` element with unique `id`, local `src`, `data-start`, `data-duration`, `data-track-index`, and `data-media-start` when trimmed. Set `muted` and `playsinline`. For image B-roll, use a real `img` element with unique ID and explicit timed duration/start/track.
- `data-start = shot.start_sec`; `data-duration = shot.end_sec - shot.start_sec`; `data-media-start = hyperframes.media_start_sec` for video. At normal playback speed, trim offset plus requested playback duration must fit the measured source duration, including any transition handles. If not, select a sufficient take/trim or deliberately repair the edit; do not silently freeze or loop the last frame.
- Place the video/image inside a **non-timed** framing wrapper. Let the media element own playback timing. Do not nest the media in another timed scene div or sub-composition that also tries to start/stop it. Existing real sub-compositions must follow the framework's nesting contract rather than receive a second timing owner.
- Let HyperFrames own media playback. Do not call `play()`, `pause()`, or `seek()` on the video/audio. Animate only supported visual properties of a non-timed wrapper with a deterministic registered GSAP timeline; do not animate video dimensions or construct timelines asynchronously.

`data-track-index` schedules clips; it does **not** set CSS layering. Same-track clips cannot overlap. Give overlapping outgoing/incoming clips separate tracks during a crossfade or wipe, and allocate extra tracks for simultaneous overlays/SFX as needed. Use explicit CSS `z-index` and stacking contexts for visual order.

## 3. Frame B-roll for a portrait Reel

Choose layout from the actual image/clip and the message. Full-frame B-roll can briefly take over the canvas while narration continues. An inset or picture-in-picture can preserve a presenter or important diagram when the approved plan calls for it. All choices retain the selected palette, typography, frame treatment, and visual identity.

Fit the media to a deliberate frame with controlled overflow. Use `cover` when the action remains readable after cropping and adjust `object-position` to preserve the important subject, hands, tools, or object. For a landscape screen recording or diagram whose text would be cut off, use a legible `contain` layout with a designed background or a deliberate close-up. Do not stretch or crop away the detail the narration explains.

For an image, use a finite purposeful pan/zoom or valid layered parallax, with enough image area to avoid exposing empty edges. Movement must be visible and useful. A whole style-catalog poster used as a moving background still does not qualify as theme-specific B-roll.

Keep framing and scene wrappers distinct where needed: a frame may clip media edges, while captions and labels sit outside that clipping wrapper. A background/scene layer can sit below B-roll, with explanatory labels and captions above it. Check the parent stacking contexts; a large child `z-index` cannot escape a lower parent stacking context.

## 4. Preserve captions, narration, and sound

Use a separate caption/overlay layer above the B-roll. Captions remain driven by the selected final narration's actual word/segment timings. Do not reset the narration clock when the B-roll enters, repeat a caption group after a scene change, or place essential captions outside the portrait safe area. Add a restrained scrim/plate or adapt the approved palette for contrast over changing footage; keep the subject/action visible.

The approved online Google AI Studio voice continues through B-roll. Use a separate timed `audio` element for that voice or for the selected premixed master. Never run local TTS, download voice models, or use editor auto-voice; skip those commands/references in companion guides. B-roll's embedded speech/music stays muted; deliberately selected source ambience can enter as a separate controlled sound cue, following the sound-design plan. In combined work, record whether this export is picture-only or already contains final audio/captions, so downstream stages cannot duplicate them.

For separate audio tracks, preserve individual voice/SFX/music control and give overlapping cues valid tracks. For `mix.routing: premixed`, play the mixed master once and omit its component voice/SFX playback from the composition. A visual transition must not fade or restart the narration accidentally.

## 5. Transition, inspect, and record evidence

Use the selected style's supported transition with sufficient outgoing/incoming media coverage and separate scheduling tracks when intervals overlap. Follow the installed transition contract: non-timed scene/framing containers, entrance choreography, and transition-controlled scene handoff. Do not fade outgoing content away before a transition needs it or leave an opaque graphic covering the B-roll. Caption-group lifetimes are handled independently from whole-scene transitions.

During actual video production, run the existing project preflight/lint/validation workflow, then inspect the draft and final encoded output. For each required B-roll scene, examine its entry, middle, exit, and the frames immediately before/after both boundaries. Confirm:

- The file is loaded and the intended scene is visible at its recorded timecodes.
- A video advances through real source frames; an image shows its intended meaningful treatment.
- Source trim, duration, crop, action, and narration segment agree with the approved scene.
- Caption/label contrast and placement work over the moving background.
- Transitions have no unintended blank/black frames, exposed edges, stale scene layers, or frozen tails.
- Voice remains continuous, and SFX/embedded media audio are not duplicated.

Save clip/scene/asset IDs, final timecodes, inspected frame paths, and actual findings in `VERIFY.md` and `production.json.broll_requirement.evidence`. The minimum is fulfilled by a reviewed scene visible in the final video, not by an unused download, JSON flag, HTML tag, or successful lint alone. If a required scene is still missing or broken, repair the responsible composition layer and keep the output incomplete until it passes.
