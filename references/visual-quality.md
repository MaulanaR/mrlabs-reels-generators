# Visual quality and the representative sample

The accepted outcome is an understandable, deliberately composed 3D explanation. A WebGL context, high polygon count, changing pixels, successful seek test or technically valid MP4 does not establish that outcome. Read alongside `reference-analysis.md`.

## Design the action before building the room

For each narration beat, record a short visual sentence: **what the viewer notices -> what happens -> what the viewer understands afterward**. Include subject, initial state, action, resulting state, camera scale/target, estimated timing and connection to the spoken idea. If the only action is camera drift around an unchanged prop, improve the action or shorten the hold. Longer contemplative holds are fine when meaning/reading needs them; explain the reason rather than enforcing a fixed cut frequency.

Use a coherent setting, but vary establishing, medium and detail views according to the explanation. Move/stop the camera deliberately. Keep the meaningful action large enough to recognize on a phone, unobscured by a lamp, title, caption or foreground object. Extra rooms and random location changes cannot compensate for an unclear action. End a movement with a readable result; avoid continuous aimless orbiting.

## Finish the hero assets

Procedural geometry is acceptable when its silhouette, proportions, edges, construction and material make the subject recognizable. Use bevelled/rounded edges where appropriate, paper thickness and wood grain/material variation where visible. Keep wood, paper, glass and metal distinguishable through color, roughness, highlights and texture; correct overly green/yellow casts and clipped lighting. More polygons alone are not an improvement. Photorealism is not mandatory for the reference's stylized 3D grammar.

Choose a suitable rights-verifiable model or texture when a primitive-built hero asset cannot meet the approved look efficiently. Record its license, provenance, file hash, modifications and face review. Buying assets or services still needs explicit cost authorization. Imagegen remains optional for a specific texture/illustration, not complete B-roll or a replacement for the animated world. Verified text remains editable.

The packaged background gallery and `background-worlds.html` are rough location/blocking prototypes. Do not use them as the production quality benchmark or copy their primitive construction unchanged into every video. Keep the 18 locations and 54 context ideas; develop the selected scene to the standard of the actual approved sample.

## What failed in the reviewed learning-video example

These are examples of visual failures, not mandatory props for other topics:

- A row of cones and a thick route on a board looked like a toy map without useful context. Give a map meaningful readable structure or choose a clearer illustration; do not fabricate historical geography.
- Sliding a magnifier over empty ruled paper did not communicate source checking. Show a meaningful inspected item and a visible result, using accurate editable source labels instead of invented manuscript text.
- Separated torus rings read as bracelets. If using a chain metaphor, model convincing interlocking links and a clear before/action/after state. Do not imply a documented chain of narrators or scholarly argument that the verified source does not establish.
- Repeating the same desk angle for long stretches gave little new information. Change the shot/action when the narration changes meaning, preserving spatial continuity.
- Uniform yellow-green flat materials and large empty tabletop/floor areas weakened the focal point. Correct material separation, light, framing and visual density.

## Produce the 8–12 second sample first

After genuine script/source/storyboard approval, choose a representative approved narration excerpt, including a meaningful action and payoff plus the actual intended captions and audio treatment. Use actual selected Google narration or compliant source audio; do not synthesize new unapproved wording. The sample should exercise the hardest representative hero asset/material/action, not just a logo, empty establishing shot or still with a zoom.

Run the normal workflow guard for this limited preparation/sample work. Save the encoded sample and a review copied from `assets/visual-review.template.json` under `10_editing/lookdev/`. Measure actual dimensions/fps/duration and SHA-256. Review playback and at least three real frames showing before/action/result. Compare with the reference's clarity, framing, materials, action and camera treatment, not just whether both outputs use Three.js. Inspect no faces/no music/source fidelity too.

For each of the seven criteria, record an honest `passed`, `needs_work` or `pending`, concrete findings and actual local evidence paths. Record limitations; do not infer listening from a transcript or artistic quality from pixel difference. `reference_comparison` explains observed matches and remaining differences. Do not mark all criteria passed because the rendering job succeeded.

Repair a weak sample locally before presenting it as ready. Show the actual sample MP4 plus a concise assessment to the user. If the user rejects it, keep `approval.status: rejected` and revise the concrete sample; do not proceed to a full render. If the user explicitly accepts the shown sample, record their real message/time and bind approval to the exact media hash, review JSON hash and current approved review-package hash. No auto-approval, inherited script approval, gallery selection or silence counts as sample acceptance. An earlier explicit approval of this same unchanged encoded sample remains valid.

Run `workflow_guard.py <project> --full-render` before full-length asset expansion, whole-video animation/prerender or final assembly. This gate needs the accepted sample; normal guard only permits preparation and sample production. Approval of the sample does not authorize publishing or a charge.

## Maintain quality through the full video

Use the accepted sample's proportions, material language, lighting, caption treatment, action clarity and camera grammar across all scenes. The sample is a quality baseline, not the same shot repeated for every sentence. New camera angles/props can remain in the same coherent world. Do not rebuild a long video until the short sample works.

After final encoding, save a separate `11_final/visual-review.json` with `scope: final`, the actual final MP4/hash and current package hash. Review every scene and important transition for the seven criteria, using real encoded evidence and honest limitations. This is distinct from the sample review and technical validation. Run the final guard only after real review; metadata checks cannot replace human judgment or guarantee authentic approval.
