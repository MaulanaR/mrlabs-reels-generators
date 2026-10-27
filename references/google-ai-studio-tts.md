# Google narration, private key and timing

Read only for `narration.mode: tts`. New speech is Google AI Studio/Gemini TTS online only, narrating approved Indonesian explanation/meaning verbatim. Optional Arabic display is not AI tilawah. No prophet impersonation/invented dialogue, local TTS/model/backend or editor auto-voice. Permitted original source recording is imported, not synthesized, and skips Google setup.

## Key resolution

The private file is `.secrets/google-tts.env` under the installed skill, not the output project. The package provides only blank `.env.example`; no parent key is copied. The importable `scripts/google_tts_credentials.py` treats that file as data, never shell code. Prefer a nonempty GEMINI_API_KEY or GOOGLE_API_KEY in it, then configured GEMINI_API_KEY/GOOGLE_API_KEY environment in that order. Pass the chosen value explicitly to the client, avoiding SDK environment-precedence surprises.

`python <skill>/scripts/google_tts_credentials.py --status` returns readiness and selected source only, not key, access validity or quota. `resolve_key()` returns secret/source inside the process for direct client use; never print it. Do not dump environment/file contents or log auth headers. No key in prompt, manifest/request JSON, code literal, Git or public archive. Ask the user to fill the local private file/secret input when needed, never paste plaintext in chat. Keep `.secrets/` ignored and excluded from package copies.

## Request and access

First run the workflow guard. Consult current official [speech generation](https://ai.google.dev/gemini-api/docs/speech-generation), [pricing](https://ai.google.dev/gemini-api/docs/pricing), [limits](https://ai.google.dev/gemini-api/docs/rate-limits) and [authentication](https://ai.google.dev/gemini-api/docs/api-key). Select a supported prebuilt model/voice with confirmed free access and preserve consistency. IDs/schemas are not frozen: do not combine Interactions and legacy generateContent formats or assume all audio is PCM.

Prefer API with the private key. Missing key/access/quota needs user resolution, not automatic browser/provider substitution, local voice, paid requests or billing upgrade. Browser AI Studio can be used only if the user explicitly chooses that supported interface. Key presence does not establish free usage. Installation/validation does not make a live TTS call.

Save `05_tts_request.json` with exact approved text, actual model/voice/interface, script version/hash, separate non-spoken direction, actual non-secret settings and observed IDs. It is a local production record, not an assumed API import format. Narration is clear calm Indonesian with natural pauses, no added introduction/ending, impersonation or recitation.

Inspect actual response MIME/encoding, decode/save returned audio under `08_voiceover/`, preserve numbered takes, probe and listen to wording/omissions/pronunciation/endings. Correctly wrap raw PCM only when actually returned; preserve documented containers directly. Never invent sample rate, extension, alignment or completed result.

## Genuine timing and recovery

Use available authorized actual-audio alignment without installing heavy models. Otherwise generate approved verbatim sentence/scene slices with the same voice/direction, measure each and join with recorded pauses; derive real segment intervals and use segment captions. Never distribute word timestamps evenly. Keep frozen approved writing unchanged; non-spoken pronunciation/timing metadata stays separate. Spoken rewrites return to review.

Selected audio controls all animated scenes/captions/SFX and the closing duration. Keep original audio and premix distinct; re-time dependencies after a new take/cut. Metadata/transcripts alone do not prove listening review.

On timeout inspect existing result before resubmitting. Within confirmed free access allow at most two extra attempts per failed/defective request, preserving accepted audio. Persistent/exhausted quota stops affected production with real state saved. Never fall back to local voice or relabel generated local speech as Google. Original source recording remains valid only if compliant with religious/no-music rules.
