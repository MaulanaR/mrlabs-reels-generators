# Contextual free SFX

Read while planning the storyboard, acquiring sound assets, and mixing the final edit. Use small local audio files selected for a specific action or setting. No local generative sound model is needed. Narration remains Google AI Studio TTS; its speech request and the SFX library workflow are separate.

## Plan sound with the script

Choose sound by the actual subject/action first, then adapt its material and intensity to the visual style. A forest ambience fits a forest scene; a digital click fits a deliberate interface or diagram event. A technology topic alone does not justify typing under unrelated imagery. Do not infer real environmental recordings from illustrative footage or present added effects as documentary evidence.

For a 30-40 second Reel, start with roughly 4-8 discrete accents as an editorial suggestion. Fewer can be appropriate. Ambience is a separate sustained layer. Leave space around narration and emotional pauses; avoid an effect on every caption word or cut. Honor `mode: none` when the user requests no SFX.

| Visual/story event | Useful sound | Timing anchor |
| --- | --- | --- |
| Hook or major fact reveal | Short restrained impact | Reveal/impact frame |
| Card, icon, or list item appears | Soft click, tap, or pop | Visible arrival/settle |
| Diagram completes a connection | Tick or short pulse | Connection completion |
| Major scene change | Brief whoosh or material sweep | Transition's main movement |
| Result or solution is revealed | Small chime or resolved tone | Result appears |
| Visible real activity | Matching foley: typing, mechanism, paper, water | Actual visible action |
| Location that benefits from atmosphere | Matching room/nature ambience | Scene entry/exit with fades |

Record sound direction in `DESIGN.md` and intended cues in `03_storyboard.md`; show meaningful SFX moments with the script review. Before approval, only plan/search or inspect existing local files. After valid script approval, reuse known-rights assets or download selected effects. Sound selection, gain adjustments, and cue repairs that preserve the approved story do not require another script approval.

## Sound character for the 15 styles

These are new production choices, not listening-derived descriptions of the five reference Shorts. The original audio/SFX were not audited. Adapt or omit any sound whose character conflicts with the actual theme.

| Style ID | Suggested character |
| --- | --- |
| `light-explainer` | Soft taps/pops, light paper movement, restrained confirmation chime |
| `dark-editorial` | Dry clicks, short low impacts, quiet textured sweeps |
| `dark-workflow` | Clean interface clicks, connection ticks, brief completion tone |
| `presenter-editorial` (Faceless Editorial) | Sparse editorial ticks and page/source reveals; room for the narration |
| `product-metrics` | Precise interface ticks, short progress accents, understated success tone |
| `swiss-kinetic` | Tight percussive taps locked to major typography beats |
| `paper-cut-story` | Paper rustles, page turns, soft cardboard taps |
| `blueprint-lab` | Pencil/sketch textures, measurement ticks, clean mechanism accents |
| `cinematic-noir` | Sparse low impacts, short restrained risers, scene-specific atmosphere |
| `pastel-3d` | Rounded plops, soft bounces, delicate bell accents |
| `comic-pop` | Playful pops and short punch accents with controlled loudness |
| `luxury-minimal` | Very sparse tactile clicks, gentle swells or one delicate chime |
| `retro-terminal` | Short keyboard/switch clicks and muted digital blips |
| `nature-documentary` | Location-appropriate nature ambience and visible-action foley |
| `collage-editorial` | Paper cuts/rustles, tape peel, camera click only for a fitting event |

## Acquire selected free assets

Reuse suitable local sounds with recorded usage rights before downloading duplicates. For new selections:

1. Use [Mixkit SFX](https://mixkit.co/free-sound-effects/) first and [Pixabay SFX](https://pixabay.com/sound-effects/) as a fallback. Search for the event/material and duration, for example "soft interface click", "paper page turn short", or "gentle water stream". Inspect actual asset pages and audition candidates when audio playback is available. Do not invent direct media URLs or an SFX API.
2. Check the current [Mixkit Sound Effects Free License](https://mixkit.co/license/modal/sfxFree/) or [Pixabay Content License](https://pixabay.com/service/license-summary/), plus any relevant asset terms. Use only free assets whose use in the intended video is supported. A "royalty-free" label alone does not mean free to download.
3. Download only the selected small files through the supported site/browser path. Run the existing script-approval checker first. Save numbered originals such as `09_edit/sfx/01_soft-click.wav`; keep any trims/conversions separately. Record the actual source title/page, creator when shown, observed download URL when available, license URL/name, access/download dates, attribution requirement, and local file hash. Preserve a local license/source receipt under `09_edit/sfx/licenses/`.
4. Probe actual duration/streams and reject damaged, misleadingly named, unrelated, or unwanted vocal/music content. Record the accepted local file and the cue-file asset ID in `production.json.assets` as `type: sfx`. Register measured properties and source details in `sfx-cues.json`.

Mixkit permits incorporating free SFX into commercial/social videos, but prohibits redistributing the standalone effects in tools/templates or source files. Keep those raw files in the user's private local project; do not bundle them into the skill or an externally shared editable archive. Provide the rendered mix and source/re-download records where needed. Apply Pixabay's current standalone-distribution restrictions as well. Never promise that an asset cannot receive a platform claim.

Try up to three suitable candidates for a cue; reuse a sound across compatible cues when appropriate. If no usable free asset is accessible, mark an optional cue `omitted` with its reason and continue. An explicitly required sound remains unresolved until fulfilled or the user changes it. Do not buy assets, sign up for a paid plan, bypass site controls, or download a large pack to fill a sparse plan.

## Cue file contract

Copy `assets/sfx-cues.template.json` to the project's `09_edit/sfx-cues.json`. Paths inside it are relative to the project root. It is a local editing record, not a provider import format. Keep arrays empty until actual project cues/assets are known; the template's null values are not measured data.

Record current script version/hash, selected narration path/hash and measured duration, selected style, and the actual composition revision (a local revision label or file hash). `status` can progress through `planned`, `acquired`, `timed`, and `mixed`; `timing_status` is `provisional`, `resolved`, or `stale`. Accepted assets may be reused after a retime.

Each `assets` entry needs an ID, actual project-relative file path, acceptance status, source/license fields described above, file hash, and measured duration/sample rate/channels. Each cue needs:

- `id`, `scene_id`, `role` (`accent`, `transition`, `foley`, or `ambience`), `purpose`, and concrete `search_terms`.
- An `anchor` with `type`, `id`, and `offset_sec`. Prefer a stable named `visual_event` from the storyboard/composition, such as a connection completion. `speech_word` anchors require real word alignment; `speech_segment` anchors require measured segment boundaries. Identify the exact intended occurrence, not an ambiguous repeated word.
- `required` (false unless explicitly required), `asset_id`, `start_sec`, `end_sec`, `trim_start_sec`, `trim_end_sec`, `gain_db`, `fade_in_sec`, `fade_out_sec`, `loop`, and `status` (`planned`, `ready`, or `omitted`). Before acquisition/timing, unknown asset/timing/gain fields are null. Omitted cues include a reason.

`start_sec`/`end_sec` are playback times on the final timeline. Trim values refer to the selected source asset; account for leading silence so the audible attack aligns with the event. Preserve a deliberate tail or fade. A loop is allowed only for suitable sustained ambience with a clean crossfade; do not loop short accents to fill time. An asset can support multiple cue IDs at different times.

After narration or animation changes, mark timings stale and resolve affected cues again. Never reuse draft seconds or evenly divide the script duration. Before mixing, every active cue must point to an accepted asset and have real intervals within the final video duration, deliberate gain, and compatible trim/fade settings. Count discrete accents separately from ambience; the 4-8 suggestion is not a validator rule.

## Mix and review

Use the existing HyperFrames audio controls or local FFmpeg, choosing the actual supported route. Keep voice, SFX, and optional music independently controlled during composition. Avoid more than two simultaneous accents by default. Match disparate source levels before placing them; reduce or duck effects when speech becomes less clear. Gain settings are deliberate per-asset decisions, not a universal number applied to every download.

Apply short fades where needed to prevent clicks, without blunting an important attack. Preserve the original TTS file. If pre-mixing, save a separate master such as `09_edit/audio_mix.wav` and set `mix.routing: premixed`; the composition then plays that master once instead of also adding its component voice/SFX tracks. For separate composition tracks, record `mix.routing: composition_tracks` and their actual sources once.

Review the final encode against every cue: correct scene/action, audible attack sync, appropriate intensity, readable speech, clean fades/tails, and no unwanted repeats or clipping. Compare narration-heavy moments with and without effects when necessary. Record inspected cue IDs/timestamps, changes, omissions, and actual mix measurements in `11_final/VERIFY.md`. If playback/listening is unavailable, report that limitation rather than claiming auditory review from a waveform or transcript.
