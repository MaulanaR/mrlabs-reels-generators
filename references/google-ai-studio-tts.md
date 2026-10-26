# Google AI Studio TTS narration

Read only when new synthesized narration is requested (`narration.mode: tts`). A source-video edit preserves original recorded speech by default (`mode: source_audio`) or remains without narration (`none`); skip this reference and all TTS setup in those modes. Generate new speech online with Google AI Studio/Gemini TTS using a prebuilt voice and free access. This is the only speech-generation provider for this workflow. Set `execution: online`, `allow_local_generation: false`, and `automatic_fallback: none`. Never install, probe, start, or use a local voice backend/model, including through a companion editor or an old request file. Provider policy does not bypass script/edit-plan approval.

## Choose the available interface

1. Run `scripts/check-script-approval.py` against the project before any speech request. Use only the approved spoken text; preserve the approved file and its hash.
2. Check current [speech-generation documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [pricing](https://ai.google.dev/gemini-api/docs/pricing), and the account's [active limits](https://ai.google.dev/gemini-api/docs/rate-limits). Model names, voices, schemas, and free availability can change. Resolve a supported TTS model with free access at production time; the template leaves model and voice unset until then.
3. Prefer the API for automation when an authorized `GEMINI_API_KEY` (or explicitly configured equivalent) is available and the project's free-tier access is confirmed. Check only whether a credential exists; never print it. Read [Google's authentication guidance](https://ai.google.dev/gemini-api/docs/api-key) when setup is required. A key's existence alone does not establish billing tier or usable quota.
4. Otherwise use the speech-generation interface in the user's signed-in [Google AI Studio](https://aistudio.google.com/) through the available browser tool/skill. Follow the current TTS link from the documentation rather than assuming a fixed deep link. Do not require an API key solely for browser use. Login, unavailable browser control, or lack of free access can require user interaction; save state and explain the exact missing prerequisite.

Use one supported prebuilt voice, preferring the user's chosen voice. Otherwise select an available clear voice suitable for Indonesian narration and record its actual name. Keep it consistent across takes/scenes. Do not create or replicate a custom voice unless requested.

## Prepare and submit the approved narration

Save `05_tts_request.json` as a local production record with:

- `provider: google_ai_studio_tts`, `execution: online`, `allow_local_generation: false`, `automatic_fallback: none`, actual `interface` (`api` or `browser`), `billing_mode: free_only`, model ID, voice name, and language.
- Script version and approved SHA-256; exact spoken `text`; separate `delivery_direction`.
- Actual `request_body` for API mode, or submitted browser controls/settings for browser mode. This record is not itself an API schema or a file that AI Studio necessarily imports.
- Attempt/take number, requested local output path, and observed request/result identifiers when available. No credentials or authorization headers.

Use the spoken script without Markdown headings, scene IDs, timecodes, or production notes. Removing non-spoken document formatting is allowed; do not paraphrase the narration. Keep delivery settings separate so they are not read aloud. A useful Indonesian default direction is: "Bacakan persis teks naskah dalam Bahasa Indonesia. Nada jelas, hangat, dan percakapan; tempo mengikuti makna, dengan jeda alami. Jangan menambah pembuka, penutup, atau kata lain." Adapt emotion and pace to the approved theme/style without changing words.

For API mode, use the current official request/response example for the selected model. Speech schemas can differ between model generations; do not combine legacy `generateContent` fields with an Interactions request. For browser mode, select single-speaker TTS, put narration in the script field, and delivery guidance in the supported style controls. Submit only after the approval gate passes.

Save/decode the actual returned audio to `08_voiceover/`, preserving numbered alternatives and the original download. Inspect MIME/encoding and the documented output structure: a WAV/container can be saved directly, while raw PCM needs a correctly specified container. Do not invent a sample rate, extension, completed job, or download path. Probe the resulting file and record its measured duration, MIME, selected take, and local path in the manifest.

## Timing on a lightweight PC

TTS output is not evidence of word alignment. Use genuine word/segment alignment if an available tool provides it without installing a heavy local model. Do not send audio to a different cloud provider automatically.

If no alignment tool is available, generate the approved narration in natural sentence/scene segments using the same voice/direction. Each segment must be a verbatim slice of the approved narration, in order, with no omissions, additions, or duplicated words. Measure each file, join them with deliberate recorded pauses, and derive segment intervals from those actual boundaries. Use segment captions and `timing_precision: segment`; never invent karaoke word timing by dividing duration evenly. When changing from a full take to segmented takes, retain the full take and rebuild timing for the selected version.

Review actual speech against the approved wording, including numbers, abbreviations, pronunciation, pauses, truncation, and the final sentence. Check audio continuity when joining segments. A transcript or duration measurement alone does not prove a listening review. Regenerate only failed takes/segments; a spoken-script rewrite returns to user approval.

## Limits and resume

The default is free access only. Do not attach billing, upgrade a plan, use an unverified paid tier, or change providers automatically. If quota is exhausted, record the observed limit/reset information and preserve the project. An explicit temporary retry time may be followed once; persistent/exhausted quota needs a later user-directed retry, not a busy retry loop.

After a timeout, inspect existing results before resubmitting. For transient failures or a defective take, allow at most two additional attempts within confirmed free access. Preserve accepted online audio and approval on resume. Missing login/key/access/quota blocks requested TTS, not source editing with original speech. Do not run local TTS/editor auto-voice as recovery. Keep locally synthesized/unknown generated takes untouched; select verified online speech when synthesis is needed. Original user-recorded audio remains valid in source mode. Local decoding, conversion, joining and mixing are allowed and must not synthesize speech.
