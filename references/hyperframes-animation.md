# Build the animated visual narrative in HyperFrames

Read the installed HyperFrames/CLI, GSAP, captions and transition guidance plus DESIGN.md, `motion-3d.md` and `visual-direction.md`. Resolve actual supported APIs and media/timeline contracts at production time. This document does not establish that a render or WebGL capture has succeeded.

## Scene design

Each approved narration beat has a visual purpose, setting, action, readable objects/text, camera/object motion and a transition into the next beat. Build the main world from actual Three.js geometry with solid objects in a coherent environment. Use editable HTML/CSS/SVG for overlays and supporting diagrams. Read `reference-analysis.md` for the inspected visual target. Examples: a door gently opening to explain hospitality, a spatial path to explain choices, or a calm room with purposeful object interaction. Match religious claims and context; avoid decorative motion unrelated to the meaning. Choose a contextual background profile/variant per beat from the catalog or describe a custom setting. Vary scene zones, props, shot scale and camera while retaining a coherent world; no repeated wallpaper or arbitrary location jumps.

The main visual target is lightweight grounded true 3D; require successful supported capture before proceeding with long production. Keep meaningful object/camera changes smooth, with stable framing, acceleration/deceleration and reading time. CSS transforms/parallax are 2.5D and must be labelled accurately. A static background plus moving subtitles, floating line icons or text cards alone is insufficient visual animation. No B-roll insertion, source-footage quota or image slideshow is needed.

Prophet markers are nonhuman abstract light with the verified name centered in an editable text layer. No body/silhouette/portrait, including on textures, reflections or secondary objects. All other no-face/no-music rules apply.

## Timing and resources

Use actual selected narration or reviewed source EDL as the master timing. Record scene IDs, measured start/end, narration/claim IDs, visual action/method and actual component IDs in `06_scene_assets.json`. Resources are optional: bind any to true asset IDs and local served paths, not invented files.

Use a visible root composition and the installed framework's registered synchronous paused GSAP timeline. Derive all motion from composition time. Three.js updates must follow the supported composition-clock capture integration; no independent wall-clock or unseeded simulation. Verify capture before building a dependency on WebGL. Unsupported capture is a blocker or requires an honestly described, reviewed change in approach; no silent downgrade to a flat infographic.

Follow framework timing ownership: one timing owner per element, explicit supported start/duration attributes, non-timed framing wrappers where needed, and no manual media play/pause/seek. Scheduling tracks and CSS layering are distinct. Give overlapping timed media separate tracks; use explicit stacking contexts for scene, light, labels, caption panel and credits. Pre-rendered authored 3D components retain editable source and measured properties; they are not stock cutaways.

## Captions, sound and continuity

Captions are a separate legible overlay above the animated scene: subtle border, rounded panel near 24 px at 1080 px, max two lines and actual word/segment timing. Keep Arabic quotations and source labels separate. One caption owner and one final audio mix; Google narration or compliant original speech continues through scene changes. Bind nonmusical SFX to relevant object actions and keep speech clear. No editor auto-voice or music.

Plan outgoing and incoming scene coverage through each transition. Do not expose blank frames, abruptly hide needed content or let decorative layers obscure narration-related action. Include the closing username and exact approved CTA in the full duration.

## Actual render review

Run supported lint/validate/inspect, then review encoded hero frames, scene entry/middle/exit and both sides of transitions. Seek forward, backward and repeatedly to the same timestamps to check deterministic state. Verify actual object/camera animation, no blank edges, subtitle contrast, prophet names, no faces/reflections, no music and continuous narration.

Save scene IDs, actual output timecodes, inspected frame paths and findings in `11_final/VERIFY.md`, `motion` review and quality/policy evidence. Motion evidence replaces the former B-roll acceptance step; do not invent asset/clip receipts for procedural scenes. Passing metadata or lint alone does not prove the final visual or listening review.
