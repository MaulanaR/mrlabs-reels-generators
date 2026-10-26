# Edit the user's original video

Use when the user supplies footage to edit, not merely a style reference. Set `workflow_mode: source_video_edit`. Build on that footage and its message; add contextual information, synchronized subtitles, motion graphics and relevant B-roll in one coordinated edit. Keep the user's selected Higgsfield/HyperFrames/Remotion pipeline. Do not replace their recording with a newly generated story or new voice.

## Intake and source inspection

- Accept attached media, exact accessible local paths, or an authorized downloadable source URL. Preserve originals; do not overwrite/move them. Cache authorized source acquisition under `00_source/` or reference the exact original path. Acquiring/inspecting the supplied input for analysis is allowed before approval; production B-roll/SFX acquisition and renders still wait.
- Clarify a missing required source or ambiguous reference-versus-input role. If several files exist, record their intended order/roles instead of picking a similarly named workspace video. A source video supplies the subject; no separate theme is mandatory. Ask only about a missing goal that materially changes the edit.
- Record a stable source ID, original path/URL and filename, SHA-256, measured duration/dimensions/fps, video/audio stream selection, orientation/rotation, and source role in `source_video.files`. Record proxy/conformed paths separately from originals. Probe variable frame rate/rotation and preserve a mapping if a proxy changes timestamp behavior.
- Read/use `watch` for frames, scene/context and transcript inspection, and relevant `edit-video` guidance for source preparation. Reuse existing matching captions/transcripts first. Otherwise use an available authorized transcription route: speech recognition is not voice synthesis, but do not install heavy speech models or upload private footage/audio to a new cloud provider automatically. Explain any missing transcription prerequisite; never invent speech or word timings. An available transcript/manual segment review can support segment captions.
- Save the source transcript with real source timestamps, uncertainty labels and selected source IDs/streams. Inspect what actually appears, important on-screen UI/text/actions, existing burned-in captions, face/action framing and the original audio. For long inputs, identify and inspect candidate passages in context; propose excerpts before applying them. Do not force a long source into a 35-second template.

Default audio is `source_audio`: preserve recorded speech, delivery, face/identity and meaning. Set `narration.mode: source_audio`, `provider: source_media`, `execution: imported`, and source asset/stream references; clear unused Google model/voice/auth/request fields. Keep `allow_local_generation: false` and `automatic_fallback: none`: they prohibit synthesis, not playback of a recording. No Google login/key/quota is needed for this mode. A source without speech can use `mode: none`; do not add a voice automatically. New/replacement narration requires an explicit user request, approved exact wording and Google AI Studio TTS online. Never clone or synthesize the original speaker by default.

## Review the plan before production

Save `03_storyboard.md` as the timed edit plan. For every proposed beat show:

| Item | Required content |
| --- | --- |
| Source passage | Source ID and actual in/out timecodes, transcript excerpt and relevant visible action |
| Output placement | Proposed output interval and intended relationship to any cut/transition |
| Information | Exact explanatory label, callout, diagram, comparison or added fact; source link for new factual claims |
| Subtitles | Actual spoken wording, language, placement/style and real word/segment timing precision |
| Motion | A purposeful reveal, highlight, arrow, zoom or diagram anchored to the speech/action |
| B-roll | Subject/action, source route, full-frame/inset/split-screen treatment and return to original footage |
| Audio/SFX | Preserve-source decision, optional cue and any explicitly requested new narration |

Show source cuts, reorderings, removals and reframing explicitly. Preserve footage order and spoken content by default; silence/mistake detection only proposes changes. Do not cut a demonstration, emphasis, qualification or sentence ending simply to improve pace. A subtitle corrects transcription errors against the recording, not the speaker's meaning. Additional information belongs in a clearly distinct overlay; do not silently insert it into the verbatim subtitles.

Create `04_edit_review.md` containing the full selected source transcript (or verified excerpts for the requested edit), source IDs/hashes and selected passages, exact planned cuts/reordering, overlay/added-spoken text, and timed layer/B-roll plan. Set `files.script` to this document and `source_video.edit_plan_path` to the storyboard. The existing `script_version`, SHA-256 and `script_approval` fields/checker apply to this review artifact; they do not require a newly authored narration. Show its concrete content in chat and ask: "Apakah transkrip, rencana potongan, dan penambahan informasi/subtitle/motion/B-roll ini sudah sesuai? Jika setuju, saya edit dengan audio asli dan editor pilihan Anda."

Record only actual user approval for that version/hash. If new spoken wording is requested, include the exact wording in the approved review artifact before TTS. Material source substitutions, new cuts that change content/order/meaning, or new factual claims need updated review/approval. Minor crop, caption transcription corrections faithful to the recording, layout and sync repairs can proceed within the reviewed meaning; when updating the hashed artifact, record the actual user's coverage rather than fabricating a fresh message. Keep the approved artifact immutable and record purely technical corrections separately.

## Build one coherent timeline

Create a source-to-output EDL at `09_edit/source-edl.json` before assembly. Each kept interval records source ID/hash, source in/out, output in/out, selected audio stream and any deliberate speed change. At normal speed, source and output lengths agree. For example, keeping source seconds 10–18 at output 0–8 maps a source caption at 12 seconds to output 2 seconds. Keep source timestamps and derived output timestamps separately; never reuse original timestamps after cuts as if the output clock were unchanged.

Retiming applies to subtitles, information overlays, motion anchors, B-roll, SFX and original audio together. Split/rebuild a cue crossing a cut; remove cues belonging to deleted speech. Keep captions based on genuine measured word/segment intervals and preserve the last spoken word. Do not silently time-stretch the original speaker; record any specifically approved retime and rebuild all dependent intervals. Use actual output timing after the EDL, rather than generating a TTS track just to obtain timestamps.

Place the layers together deliberately:

1. **Original footage:** remains the main visual source and returns after inserts. Protect the important speaker, product, demonstration, UI or action. Keep source aspect/framing unless the user requested a new format; show the proposed crop/contain layout for a portrait adaptation.
2. **B-roll:** acquire relevant internet footage/photos after approval and preserve at least one qualifying scene per full Reel by default. It can cover the main picture briefly or appear as an inset/split-screen while original speech continues. User-provided cutaways with the right subject can also qualify; main presenter footage or unused downloads do not.
3. **Information and motion:** add explanatory labels, highlights and diagrams tied to what is actually said/shown. Keep new sourced context distinct from the source's own claims. Never fabricate UI, quotes, statistics or evidence. For uncertain speech, mark/review it instead of inventing an authoritative graphic.
4. **Subtitles:** remain legible above footage/B-roll in the safe area. Coordinate placement with information and motion so they do not cover a face, meaningful action, UI, or each other. A brief full-frame B-roll insert need not show every overlay simultaneously; subtitle/audio continuity and a clear visual hierarchy matter.
5. **Audio:** play each approved source interval once, in sync with the matching main-picture interval. In HyperFrames use muted video plus separate source audio with the same source trim/start/duration. In other editors follow supported audio routing. Mute embedded B-roll speech/music; preserve original source audio under inserts. Add SFX only when useful and keep speech intelligible. Picture-only handoffs plus one final audio/caption owner prevent duplicates across editors.

Style 04's no-person rule applies to added/generated visual assets. Do not erase an existing original presenter or discard their source just because that style was selected; preserve the original or clarify an explicit requested faceless conversion. Respect any user-specified feature limits: a subtitle-only request uses the specialist workflow without forcing B-roll, motion, cuts or TTS. Record that explicit scope override (including `min_scenes_per_video: 0` when appropriate).

## Verify and resume

Before render, restate the exact source filenames/IDs and intended output path in the project notes and check them against the approved review artifact. Confirm the same source was actually used. Reuse accepted transcripts, media, EDL and approval on resume; a supplied recording must never be rejected as forbidden "local voice" or relabelled Google TTS.

Inspect the final encode: recognizable original identity/action, faithful speech, intended cuts only, source/output transcript mapping, lip sync and audio continuity at cuts and B-roll entry/exit, readable/noncolliding overlays/subtitles, actual B-roll movement/crop and no duplicate audio. Record source hashes, EDL version, inspected intervals and source/output evidence in `VERIFY.md`. Preserve the original and output transcripts, EDL, information-source notes and editable projects alongside the final MP4. Report missing transcription/listening/render checks accurately.
