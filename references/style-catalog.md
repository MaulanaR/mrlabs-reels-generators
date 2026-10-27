# Islamic background catalog

18 contextual environment profiles and 54 named starting variants are active in `style-catalog.json`. These are a starting library, not a restriction to those locations. Choose per approved narration beat; a project-level profile supplies a shared visual identity rather than one wallpaper for the whole video. The parent's generic styles remain retired.

| Number | Profile ID | Environment |
| --- | --- | --- |
| 01 | azab-mencekam | Ruang gelap, kabut tipis, arsitektur batu dan cahaya terarah. |
| 02 | gurun-siang | Pasir berlapis, langit siang dan batu hangat tanpa figur. |
| 03 | masjid-tenang | Lengkung arsitektur, halaman teduh dan sinar siang lembut. |
| 04 | kota-keseharian | Bangunan kota dan material keseharian dalam cahaya pagi. |
| 05 | rumah-hangat | Jendela, cahaya hangat, meja dan benda rumah yang relevan. |
| 06 | sungai-tafakkur | Aliran sungai dan lapisan alam yang tenang, tanpa fauna berwajah. |
| 07 | hutan-hujan | Pepohonan berlapis, tanah basah dan sinar menembus kanopi. |
| 08 | pegunungan-fajar | Punggung gunung berlapis, lembah berkabut dan cahaya fajar. |
| 09 | laut-senja | Pantai terbuka, horizon laut dan cahaya senja yang tenang. |
| 10 | kebun-subur | Petak tanaman dan jalur kebun dengan tanah serta dedaunan tanpa fauna. |
| 11 | pasar-amanah | Kios tanpa figur, timbangan dan peti barang generik tanpa merek. |
| 12 | ruang-belajar | Meja belajar, lampu dan buku tanpa teks/ilustrasi wajah yang ditanam. |
| 13 | bengkel-kerja | Meja kerja, alat generik dan material kayu/logam tanpa figur. |
| 14 | halaman-hujan | Halaman rumah, kusen pintu dan permukaan basah saat hujan lembut. |
| 15 | malam-berbintang | Langit berbintang, horizon bukit dan ruang malam tanpa simbol kesakralan. |
| 16 | jalan-persimpangan | Jalan bercabang dan objek penunjuk editable sebagai metafora pilihan. |
| 17 | perpustakaan-ilmu | Lorong rak, buku polos dan ruang baca generik tanpa klaim lokasi sejarah. |
| 18 | lembah-badai | Batu lembah, langit berat dan gerak kabut tanpa rincian gaib rekaan. |

## Selection and variation

- Match each scene to the actual action, place, time and meaning of the narration. Custom environments are allowed when more suitable; do not force a desert, mosque or dark scene onto unrelated daily life.
- Prefer a varied sequence when the discussion changes context. Within one location, vary the zone, props, shot scale, foreground/depth, camera path or lighting rather than inventing a location jump. A close-up, wider spatial explanation and new object interaction can keep a coherent room visually varied.
- Use time of day and weather only when context supports them. Do not imply an undocumented historical detail, a real location identity, passage of time or a divine sign just to vary the image. Darkness/bad weather does not establish that a real disaster is punishment.
- Keep palette/material language and smooth spatial transitions coherent. Change at narration/story boundaries, not random fixed-second background swaps or flashing color cycles. Respect an explicit user request to remain in one setting.
- Avoid reusing the same scene geometry/framing unchanged across the whole video. A new gradient alone is not a meaningful environment variation. Each scene still has purposeful authored animation, not B-roll or an image slideshow.

In the reviewed storyboard and working `06_scene_assets.json`, record `background_profile` (or a custom ID), `background_variant`, `context_reason`, setting/era, light/weather, key objects, shot/camera and transition. Describe custom variants explicitly. Estimates can be resolved to actual narration timing after approval; material setting/meaning changes need revised approval.

## Show the relevant previews

Show up to three relevant individual PNGs with absolute Markdown paths, and offer `assets/style-gallery.html` for all 18. The gallery contains an example invocation and the three named variants for each profile. Boards are grouped to remain readable:

- `assets/islamic-background-board.png`: profiles 01–06.
- `assets/islamic-background-board-02.png`: profiles 07–12.
- `assets/islamic-background-board-03.png`: profiles 13–18.

There is one static preview per profile, not a separate image for each of the 54 variants. These are static native Three.js WebGL environment renders, not final animated HyperFrames captures, religious evidence or full-video backgrounds. The preview scene source is `assets/background-worlds.html`; its local runtime is pinned to r180 with MIT license/source receipts under `assets/vendor/`. Author editable layered scenes from narration. No Arabic/prophet lettering or username is baked into previews. Only an approved prophet scene receives its abstract light/name marker.

Read `visual-direction.md`, `motion-3d.md` and `reference-analysis.md`. Every profile retains no faces/no prophet bodies/no music, verified editable Arabic, rounded captions, actual user credit and actual-audio timing. HyperFrames remains the editor.
