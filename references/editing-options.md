# Choose Higgsfield, HyperFrames, Remotion, or a combination

Read during brief/script review and again before opening an editor or rendering. Editor selection is independent of the 15 visual styles and `render_route` (motion versus hybrid assets). All routes use Google AI Studio TTS online, internet-first B-roll, the same approved script, and at least one relevant B-roll scene per final video. Disable every editor's narration generation/auto-voice feature. Do not start or install local speech synthesis.

## 1. Offer and record the user's choice

| Choice | Intended editing work | Prerequisite |
| --- | --- | --- |
| Higgsfield | Edit accepted footage/assets in Higgsfield Video Editor/Katana through supported editor tools | Installed Higgsfield skill, preset resolver, and the editor plugin/runtime required by `/use-video-editor` |
| HyperFrames | HTML/GSAP graphics, timed footage, captions, effects, and final assembly | Installed HyperFrames composition/CLI guidance and working renderer |
| Remotion | React compositions, footage sequences, captions, animation, and final assembly | Supported Remotion/React project, matching package versions, Node/browser rendering dependencies |
| Gabungan | Any explicit pair or all three, with a defined job per engine and one final assembler | All selected engines and a supported media export/import path between stages |

If unspecified, ask: "Untuk editing, pilih Higgsfield, HyperFrames, Remotion, atau gabungan? Kalau gabungan, sebutkan tools yang ingin dipakai, atau pilih semuanya." Reuse an explicit choice in the current brief or resumed project. Do not infer HyperFrames from a style profile, previous default, or a downloaded asset. Draft the script while waiting, but keep production pending until selection and script approval are both real. Selecting an editor does not approve an unseen script.

Write `production.json.editing`:

- `selection_status`: `pending` or `selected`; `selection_message`: the actual user instruction, never fabricated.
- `mode`: `higgsfield`, `hyperframes`, `remotion`, or `combined`; `engines`: the selected names in planned execution order.
- `final_assembler`: exactly one selected engine. For combined work, propose it with stage responsibilities before production; honor an explicit user preference.
- `project_paths`: actual project-relative folders for only selected engines. New projects use `10_editing/<engine>/`; preserve old paths such as `10_hyperframes/`.
- `stages`: actual stage ID, engine, purpose, input/output assets, caption/audio ownership, and observed status. Keep `handoffs` and `jobs` empty until real exports/submissions exist.

Check only selected engine dependencies. Explain a missing editor/tool/runtime and offer the available choices; do not silently substitute another engine, run an unselected engine, or claim an unavailable combination ran. Browsing/updating this skill does not open editors, upload media, submit jobs, or render.

## 2. Higgsfield route

1. Read the installed `app-6a3293e129088191abf0875820e839da:higgsfield` skill (or the current installed Higgsfield equivalent). Resolve `/use-video-editor` with the connected preset-instruction lookup before opening or working in the editor, even when the user selected it in ordinary prose.
2. Follow the returned handoff to the separate local Video Editor/Katana plugin and its supported tools. Discover current schemas and capabilities; do not invent editor commands, IDs, formats, export support, or a cloud-sandbox substitute. A local video editor is allowed; a local voice backend is prohibited.
3. After valid script approval and editor selection, import only the approved assets and the existing Google AI Studio narration. Preserve subject/message, measured narration timing, B-roll, and design. Use supported editing functions for cut, crop, graphics, captions, transitions, and SFX; confirm unsupported requirements before claiming the pipeline can deliver them.
4. Choosing Higgsfield for editing does not invoke `/ugc-video`, `/faceless-video`, or `/ad-multiplier`, authorize generation/purchases, or change the internet-first B-roll policy. Those workflows require their own explicit slash request. Never use an editor preset to synthesize new narration.
5. Honor confirmed budget limits and tool approval gates; selection alone does not authorize credits, subscriptions, or paid export. Save real project/job IDs, follow supported status/result tools, and inspect/export actual media. If tools or an export/import path are unavailable, preserve state and explain the exact blocker before substituting anything.

## 3. HyperFrames route

Read installed `hyperframes:hyperframes` (or the resolved `hyperframes`) and its CLI skill. Before HTML, read `DESIGN.md` and the typography, caption, motion, and transition references relevant to the composition. Read [hyperframes-broll.md](hyperframes-broll.md) for actual media placement, crop, overlap, and audio routing.

Use the existing online narration as separate audio; skip TTS references, TTS commands, voice download/setup steps, and auto-voice features. Build the deterministic composition in the recorded HyperFrames directory. Run the available version's composition checks, preview and render; review the actual encode. Herk resources are conditional helpers, not dependencies of every editor route.

## 4. Remotion route

Read an installed Remotion skill if available. Otherwise inspect the selected project's `package.json`, lockfile, scripts, and installed version, then use current [composition](https://www.remotion.dev/docs/composition), [Sequence](https://www.remotion.dev/docs/sequence), [audio](https://www.remotion.dev/docs/using-audio), and [render](https://www.remotion.dev/docs/cli/render) documentation for that version. No missing companion skill should be presented as an installed one. Use a supported existing runtime or explain missing setup; never add a local speech package/model as a rendering dependency.

- Keep editable React source, media and input props in the recorded Remotion project directory; use supported project-served media references.
- Register the composition with the actual ID, portrait dimensions, fps, and measured duration. Convert approved narration/shot intervals from seconds to frame boundaries consistently, accounting for sequence-relative offsets and transition overlap. Retain the source seconds and record resulting frames; do not spread words evenly.
- Place actual footage/images in sequences with explicit source trim, crop/focal point and meaningful still-image movement. Drive animation deterministically from the render frame, with no wall-clock playback or nondeterministic randomness.
- Import the approved Google AI Studio audio or premixed master using supported audio components. Mute embedded B-roll sound unless deliberately mixed. Use actual word/segment timings for captions; never generate narration in Remotion.
- Resolve CLI flags/components from the installed version and official docs. A typical local export is `npx remotion render <entry-point> <composition-id> <output-path>`. On Windows, put input props in a JSON file rather than shell-interpolated inline JSON. Use resource-appropriate render concurrency for this PC; choosing Remotion does not authorize cloud/Lambda deployment or paid services.
- Preview hero/boundary frames and inspect the exported media, dimensions, timing, captions, B-roll and audio. A React source file or successful command alone is not an accepted final video.

## 5. Combined route and handoffs

Accept any pair or all three. For example, all three can use **Higgsfield for footage assembly -> HyperFrames for graphic inserts -> Remotion for final assembly/captions/mix**. This is a proposed division, not an automatic mandatory sequence; adapt to the user's choice and supported tools. Each selected engine needs a concrete useful job. Do not re-render the same stage in every engine.

Use real exported media between engines. Do not assume HyperFrames HTML, a Higgsfield/Katana draft, and Remotion TSX are mutually importable. Keep original editable source in each engine. Export isolated graphic scenes/inserts or approved footage segments; use alpha only when both export/import paths support it, otherwise use complete scene clips. Store intermediate exports under `10_editing/handoffs/`.

For each handoff record originating stage/engine, actual source project, export path/hash, dimensions/fps/duration, destination engine/stage, source trim, and final timeline offset. Probe the export before import. Preserve useful transition handles, source framing, and the narration's global clock; avoid unnecessary resizing, frame-rate conversion and repeated lossy encoding. Keep shot IDs and B-roll provenance linked through every intermediate.

Choose one final caption owner and one audio-mix owner. Prefer picture-only intermediate clips and attach the original approved narration once in the final assembler. When a handoff intentionally contains final mixed audio or baked captions, record that fact and disable duplicate layers downstream. Rebuild dependent timing after any deliberate audio or clip retime. Review the last engine's actual encode, including the qualifying B-roll interval and handoff boundaries.

## 6. Binding and resume

For each shot's `editing_bindings`, record the real engine/stage, clip/sequence ID, asset ID, project-relative path or supported uploaded-media ID, source trim, actual timeline interval, crop/layer, and movement. Remotion also records frames; HyperFrames may retain its detailed `hyperframes` object. Bindings must match the actual editor project, not just the storyboard. Preserve source/license receipts and record final evidence in `broll_requirement` and `VERIFY.md`.

On resume, reuse an explicitly recorded user choice and accepted exports, inspect pending jobs before submitting again, and preserve unchanged script approval. An older folder/default does not prove a user choice: ask if selection evidence is missing. Add cloud-only narration policy fields; never execute an old local voice command. Keep old audio as an untouched original, but narration with local or unknown provenance is not the selected voice for new/resumed production: obtain a Google AI Studio take of the approved wording before rendering, or report unavailable access. Rebuild timing/captions/cues for the actual selected take without inventing fresh script approval.
