> Islamic override: inspect real moving frames for faces; mute embedded B-roll sound. No music or melodic ambience. This skill uses six new background profiles and HyperFrames only.

# Internet-first B-roll, generated images only when needed

Read when selecting B-roll and before any image-generation fallback. The default is suitable free footage from the internet; use an appropriate stock photo with pan/zoom when it serves the scene. Reuse suitable user-provided or already accepted assets with known rights before downloading duplicates. Do not start Flow or Gemini image/video generation for the default workflow.

## Search for the approved scene

Before approval, research candidate pages and describe the planned visual in the storyboard. Download production files or generate images only after valid script approval. Search from the actual narration segment: subject, action, setting, and crop/people requirements. Translate queries when useful. Reject human/animal faces in actual frames, reflections, screens/photos and textures. Hands, backs and faceless figures are allowed when relevant, never as prophet bodies/silhouettes. Prophets use only abstract light plus editable names.

Start with [Pexels videos](https://www.pexels.com/videos/) and [Pixabay videos](https://pixabay.com/videos/). Photos from those sources can work when deliberately animated. Other sources are usable when their actual terms support the intended use, including file-specific licenses on a source such as Wikimedia Commons. A search result or social-media upload is not permission to reuse a clip.

Use a small focused search: start with one or two query variants and inspect up to three promising candidates across suitable sources. Stop once a relevant, usable file fits. A short portrait-friendly shot that clearly explains the line is preferable to a larger unrelated cinematic download. Keep the source's actual action/context; do not mislabel generic stock as evidence of a specific person, product, place, or event.

## Verify and acquire the selected asset

Open the real asset page and current [Pexels license](https://www.pexels.com/license/) or [Pixabay license](https://pixabay.com/service/license-summary/), including applicable asset-specific terms. Confirm free use in the intended video, attribution requirements, and relevant limits. Avoid watermarked previews, paid-only files, inaccessible downloads, or material with unclear reuse permission. Do not evade a site's login, download, or access controls.

Record in `production.json.assets`:

- Stable asset ID, scene/shot ID, type (`video` or `image`), status, local project-relative path, and SHA-256.
- Provider, actual title, creator when available, original asset page URL, observed download URL when exposed, access/download dates, license name/URL, attribution text/requirement, and relevant source restrictions.
- Measured duration/dimensions and media stream properties, plus the selected trim/crop and a short content-fit review.

Save selected originals with numbered names under `07_broll_assets/`, preserving any modifications as separate files. Keep a source/license receipt there, and include required attribution in a project credits note for final handoff. Respect each source's standalone/source-file redistribution limits when sharing an editable project. Do not bundle stock media into the skill repository.

Probe/decode the local file. Inspect the frames or photo for actual subject/action, resolution, portrait crop, duration, unwanted baked-in captions/logos, and people constraints. An asset counts only after it is accepted, placed in the selected editor pipeline, and visibly reviewed in the final encode. Keep selected original source audio or online narration separate and mute embedded clip speech/music unless the mix deliberately uses it.

## Use imagegen only for a real gap

Use the available `imagegen` skill and built-in `image_gen` tool when a focused search cannot supply a usable matching asset, or the approved scene needs an original visual that stock cannot express. Record the reason and relevant sourcing outcome in `06_scene_assets.json` as `fallback_reason`. A preference for a particular palette alone is not a reason to regenerate otherwise suitable stock; framing, annotations, and style can often be applied in editing.

Keep the existing approval when the fallback preserves the reviewed subject, action, and message. A new metaphor or material story change returns to storyboard/script review. Use the per-scene prompt in [script-and-assets.md](script-and-assets.md), including exact theme, approved narration, visual purpose, subject/action/setting, style-only constraints, and exclusions. Do not fabricate factual evidence or a real product UI through generation.

For a new image, omit edit-reference parameters. For an edit, inspect the target first and supply the target image through the tool's supported reference mechanism. Prefer opaque backgrounds; use transparency only when the composition needs a cutout. Save the actual prompt and returned result, then copy the accepted file from the tool's returned location to `07_broll_assets/`; do not assume a destination argument or fabricate an output path.

The built-in route does not require a separate OpenAI API key, but depends on tool/account availability and limits. If unavailable, preserve the sourcing outcome and report the specific blocker; do not silently use CLI/API generation, install a local model, or return to Flow/Gemini. The optional CLI route needs the user's explicit choice under the imagegen skill. No image is generated merely to demonstrate this setup change.

## Edit and resume

Default source order is existing authorized assets, internet stock/source media, then a justified generated-image fallback. Internet-sourced/generated stills receive meaningful finite pan/zoom/parallax in the [selected editor pipeline](editing-options.md); source footage uses measured trim and crop. Read [HyperFrames integration](hyperframes-broll.md) only for a selected HyperFrames stage. Keep at least one qualifying B-roll scene per video across all six Islamic background profiles.

On resume, use actual paths from the manifest, preserve accepted files and source receipts, and avoid repeated searches/downloads/generation. Older `06_flow_prompts.json`, `07_flow_downloads/`, `flow_jobs`, and `visual_type: flow` can be read as legacy state; they do not authorize new Flow requests. New projects use neutral asset filenames and `asset_jobs` only for actual imagegen work. Do not delete old files or alter the approved narration just to migrate providers.
