# Smooth, contextual 3D-priority motion

Read after `DESIGN.md` and before composing motion. HyperFrames remains the final timing/editor owner. Read its installed composition, CLI, typography, captions, motion-principles and transition guides. Skip local TTS, music-generation and voice-download instructions. Resolve actual supported runtime commands and renderer behavior rather than assuming a plugin version.

## Build a useful spatial scene

- Prioritize actual topic objects, scene depth, light and camera: a doorway reveal, a path, layers of a room, water flow or a meaningful relationship. Avoid an unrelated spinning globe, random particles, decorative camera rolls and effects on every word.
- Use a light scene: simple geometry, modest texture sizes, limited lights/shadows, controlled reflections and finite particle counts. Do not install heavy local generative/speech models or require ray tracing/physics for a short explanation.
- Use actual Three.js when a scene needs real geometry, perspective camera or lighting. CSS transforms/parallax are useful 2.5D, but must be labelled as such. Flat captions stay 2D for reading. Prefer fewer meaningful 3D scenes over an overloaded frame.
- Never model prophet bodies or faces. An abstract light marker is geometry/light/particles with no human outline; the exact verified prophet name is a separate editable centered text overlay. No depiction of Allah. No unsupported literal unseen reconstruction.
- A faceless figure can reveal a face when the camera or head turns. Constrain geometry, framing and movement and inspect the entire intended action, including reflections, cast textures and transition frames.

## One deterministic clock

Build/register finite paused GSAP timelines synchronously as required by HyperFrames. Preload assets using the renderer's actual supported readiness mechanism; do not construct timelines in asynchronous callbacks. Asset readiness and synchronous timeline creation are different requirements.

Drive camera/object transforms from the composition time, not wall-clock time, a second independent requestAnimationFrame loop, automatic video playback or unseeded randomness. Apply smooth eased acceleration/deceleration, limited camera travel, a steady focal point and deliberate readable holds. Avoid infinite repeats and conflicting owners of a visual property. Respect the installed framework's entrance/transition contract.

For Three.js, inspect [WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer) and the available installed version. Use a supported render callback/integration that redraws the canvas after each timeline seek and captured frame, including backward/repeated seeks; do not assume that GSAP `onUpdate` alone runs if the capture engine suppresses callbacks. Do not invent a HyperFrames canvas-hook API. Verify WebGL, loaded fonts/textures, capture orientation, depth/color and any transparency before depending on the scene.

If direct WebGL capture is unsupported, use an actually available deterministic 3D pre-render/export path and import its real measured clip into HyperFrames. Preserve its editable source. If that path is unavailable, simplify meaningful spatial treatment and disclose 2.5D as 2.5D or report a required 3D blocker; never claim a Three.js render from an empty/black canvas or static screenshot. Local HTML preview success alone is not an encoded-output pass.

## Production review

Check hero frames, entry/middle/exit, every transition, prophet-name alignment, caption/Arabic visibility and final credits. Seek to the same timestamps twice and backward/forward; exported positions/lighting must match. Inspect actual video movement and ensure no frame exposes a face or prohibited depiction. Check clipping, empty edges, flicker, black frames and abrupt movement at scene joins.

Keep actual evidence in `VERIFY.md`, `motion.review_status` and `motion.webgl_capture_status` (`passed`, `not_used`, or an observed unresolved state). `passed` needs actual supported WebGL capture evidence; 2.5D-only work records `not_used` and the actual motion method. The background gallery contains static HTML/CSS 2.5D concepts only, not a claimed Three.js/video test.
