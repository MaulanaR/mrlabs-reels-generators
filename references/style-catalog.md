# Visual style catalog

Read this on invocation to present examples. The machine-readable source is [style-catalog.json](style-catalog.json), including image paths, palettes, fonts, motion, captions, and route. [generation-prompts.json](../assets/styles/generation-prompts.json) is solely for inspecting/regenerating the catalog samples, never for production asset selection or imagegen prompts. Its demo theme is 'Dari ide ke aksi'. All example PNGs are existing local style previews; scene imagery must come from the actual user theme and approved narration.

## Presenting examples

- Bare invocation or no theme: embed the three board PNGs below using absolute local image paths, list numbers/names, then ask for the theme. Style number/name is optional.
- Theme and an explicit style: embed that style's single PNG, state its name, and draft the script/storyboard for user approval.
- Theme without a style: show up to three relevant single-image previews with brief fit explanations, identify the automatic selection, and draft without requiring a style confirmation. Present and wait for script approval before generating any new media.
- A request for all styles: show the three boards plus the gallery link. Do not force the user to reopen the original YouTube references.
- Resolve paths against this skill's actual installed folder. Construct an absolute filesystem path to `assets/styles/01-light-explainer.png` (or the selected asset), then use that resolved path in a Markdown image embed. Do not leave environment variables or a placeholder in the rendered image URL. A plain filename or unresolved relative path will not display the local image in chat.

Boards: `assets/style-board-reference.png`, `assets/style-board-new-a.png`, `assets/style-board-new-b.png`. Interactive gallery: `assets/style-gallery.html`. The gallery can be opened locally and does not need a network connection.

## Styles

| No. | ID / name | Origin | Suitable themes |
| --- | --- | --- | --- |
| 01 | `light-explainer` / Light Explainer | R1 | edukasi, konsep, analogi |
| 02 | `dark-editorial` / Dark Editorial | R2 | AI, sistem, perbandingan |
| 03 | `dark-workflow` / Dark Workflow | R3 | developer, tutorial, workflow |
| 04 | `presenter-editorial` / Faceless Editorial | R4, adapted | review, edukasi, bukti |
| 05 | `product-metrics` / Product Metrics | R5 | produk, bisnis, benefit |
| 06 | `swiss-kinetic` / Swiss Kinetic | Original addition | kampanye, motivasi, pengumuman |
| 07 | `paper-cut-story` / Paper Cut Story | Original addition | cerita, kreativitas, UMKM |
| 08 | `blueprint-lab` / Blueprint Lab | Original addition | sains, engineering, cara kerja |
| 09 | `cinematic-noir` / Cinematic Noir | Original addition | cerita, craft, motivasi |
| 10 | `pastel-3d` / Pastel 3D | Original addition | pemula, pendidikan, produk ramah |
| 11 | `comic-pop` / Comic Pop | Original addition | edutainment, fun fact, promo energik |
| 12 | `luxury-minimal` / Luxury Minimal | Original addition | premium, arsitektur, brand |
| 13 | `retro-terminal` / Retro Terminal | Original addition | coding, teknologi retro, sejarah digital |
| 14 | `nature-documentary` / Nature Documentary | Original addition | alam, lingkungan, sains, travel |
| 15 | `collage-editorial` / Collage Editorial | Original addition | budaya, opini, cerita kreatif |

## Apply the selected style

Resolve 'gaya 03', '03', 'Dark Workflow', or its ID to one catalog entry. Record its ID in production.json and derive DESIGN.md from its palette, fonts, visual device, motion, caption guidance, and avoid list. User branding overrides tokens while preserving a coherent style.

Style 04 is now **Faceless Editorial** at the user's request: use a typographic hook, topic-specific screenshots/diagrams, and the cobalt editorial identity, without people, faces, hands, bodies, human silhouettes, or avatars. Its existing `presenter-editorial` ID and preview filename remain compatibility keys; the older name `Presenter Editorial` resolves to this updated style. Honor this no-people direction in its scene prompts and asset acceptance as well as its preview.

Use [sound-design.md](sound-design.md) for the SFX character associated with all 15 styles. Include sound direction and intended cues in the storyboard review; download selected sounds after script approval. These sound choices are proposed production directions, not an assertion that the original reference videos used those effects.

All 15 styles require at least one relevant B-roll scene per output video. A `motion` route keeps the chosen graphics style while inserting eligible footage or an animated theme-specific image. All routes follow [internet-first sourcing](internet-broll.md), with imagegen only when needed; a style does not require an external generation provider. Apply [the B-roll contract](production-contract.md#minimum-b-roll-per-video); selecting a minimalist or diagram-heavy style does not remove the requirement.

Selecting a style does not approve the script. Follow [script-and-assets.md](script-and-assets.md): first show the actual narration and scene plan, then wait for direct user approval. No production B-roll download, image generation, TTS, or render may precede that approval.

These images are static concept frames generated with the built-in imagegen tool, not copied screenshots or playable video templates. Reconstruct meaningful editable text, diagrams, and individual layers in the [user-selected editor pipeline](editing-options.md). The style registry's `render_route` describes the motion/hybrid visual treatment; it never chooses an editor. Offer Higgsfield, HyperFrames, Remotion, or a combination independently. Use relevant internet footage/photos for hybrid routes, with an imagegen fallback only if needed. Do not use the entire sample poster as a static background for the full Reel, reuse its demo wording as narration, or treat a fictional sample character as an authorized recurring identity.

For original-video edits, adapt the selected style to supplementary graphics while preserving the actual source, voice and meaningful visible action. Style 04's no-person rule controls added visual assets; it does not silently remove an existing source presenter. An explicit faceless conversion can be planned with the user. See [source-video-edit.md](source-video-edit.md).

Transfer appearance only. Do not carry the sample's bulbs, gears, terminals, wording, characters, or productivity story into unrelated topics. Prefer text style tokens and theme-specific references for an optional imagegen request; if a sample image is supplied, label it STYLE ONLY and explicitly exclude unrelated content. Generate only a needed approved scene image, not the full skill/gallery or an invented complete Reel.

Use [visual-direction.md](visual-direction.md) for the original five-video evidence and shared pacing/layout rules. Additional styles broaden the library; they do not overwrite an explicit user choice.
