# MRLabs Reels Generator

Skill untuk **Codex** dengan dua mode: **buat Reel dari tema** atau **edit video asli pengguna** dengan informasi, subtitle, motion graphics, dan B-roll dalam satu video. Editor dapat dipilih: **Higgsfield, HyperFrames, Remotion, atau gabungan**.

**Naskah atau rencana edit harus disetujui pengguna sebelum produksi dimulai. Setiap Reel lengkap wajib memiliki minimal satu adegan B-roll yang relevan.**

**Suara baru hanya dibuat secara online melalui Google AI Studio TTS jika diperlukan/diminta. Video asli memakai rekaman suara aslinya secara default.** Audio yang direkam pengguna bukan voice sintetis lokal dan tidak membutuhkan TTS/API key Google. Skill tidak menjalankan VoiceStudio, Kokoro, model pembuat suara lokal, atau auto-voice editor. Konversi dan mixing audio lokal tetap diperbolehkan.

Nama repositori adalah `mrlabs-reels-generators`, sedangkan nama skill dan perintahnya adalah **`mrlabs-reels-generator`**.

## Mulai dari sini

1. Pasang skill ini, Watch, dan dependensi editor yang ingin digunakan di bawah.
2. Siapkan pencarian/pengunduhan B-roll internet. Akses Google AI Studio hanya diperlukan jika membuat narasi baru.
3. Kirim tema **atau video asli** (attachment/path/URL yang boleh diakses), pilihan editor, dan nomor gaya jika ingin. Jika editor belum disebutkan, agent menawarkan pilihannya sambil menyiapkan naskah/rencana edit.
4. Tinjau naskah dan storyboard, atau transkrip serta rencana edit video asli. Setujui versi yang sesuai.
5. Agent melanjutkan produksi, editing, dan pemeriksaan hasil sesuai akses alat yang tersedia.

```text
Gunakan $mrlabs-reels-generator.
Tema: bagaimana AI membantu pemilik kedai kopi mengelola stok.
Audiens: pemilik UMKM.
Durasi: sekitar 35 detik, Bahasa Indonesia.
Gaya: 04 Faceless Editorial.
Editor: HyperFrames.
Buat naskah dan storyboard dahulu untuk saya setujui.
```

Skill ini berisi instruksi, referensi, aset contoh gaya, template, dan pemeriksa persetujuan. Eksekusi membutuhkan agent dengan akses filesystem, terminal, browser, serta runtime dan akun yang diperlukan. Memasang skill saja tidak memasang semua aplikasi atau memberi akses ke layanan Google.

## Alur kerja

```text
Tema
  -> Riset, pilihan gaya, dan pilihan editor
  -> Naskah lengkap, storyboard, rencana B-roll dan SFX
  -> Persetujuan pengguna
  -> Narasi Google AI Studio TTS dan aset adegan
  -> Editing dengan editor pilihan, caption, SFX, dan transisi
  -> Review hasil encode
  -> Video final dan proyek lokal yang dapat diedit
```

Sebelum persetujuan, agent boleh melakukan riset, mencari kandidat B-roll beserta lisensinya, menampilkan preview gaya yang sudah tersedia, dan menulis rencana. Pengunduhan B-roll/SFX produksi, pembuatan gambar/narasi, serta render menunggu persetujuan naskah. Memilih gaya atau mengirim tema belum termasuk persetujuan terhadap naskah yang belum ditampilkan.

Untuk video asli:

```text
Video asli
  -> Inspeksi gambar/audio dan transkrip bertimestamp
  -> Rencana potongan, informasi, subtitle, motion, dan B-roll
  -> Persetujuan pengguna dan pilihan editor
  -> Editing dengan audio asli dan semua layer yang direncanakan
  -> Review sinkronisasi dan hasil encode
  -> Video final, source terjaga, dan proyek yang dapat diedit
```

Tema boleh disimpulkan dari video yang benar-benar diperiksa. Video yang dikirim hanya sebagai referensi gaya tidak otomatis menjadi sumber produksi. File asli tidak ditimpa; sumber yang dipilih, potongan, dan perubahan framing dicatat. Durasi/bahasa/isi asli dipertahankan kecuali pengguna meminta perubahan. Tidak otomatis menulis ulang ucapan, memotongnya menjadi 35 detik, mengganti suara, atau membuat video lain.

Informasi tambahan diberi sumber faktual dan dibedakan dari subtitle verbatim. Motion mengikuti ucapan/aksi. B-roll dapat menjadi insert, inset, atau split-screen sambil suara asli tetap berjalan; subtitle dan informasi diatur agar tidak saling menutupi wajah, demonstrasi, atau UI. Sesudah potongan, semua timing diperbarui melalui catatan source-ke-output (EDL). Lihat [panduan edit video asli](references/source-video-edit.md).

## Instalasi

### Pilihan 1 — minta Codex memasang skill

Salin permintaan berikut ke Codex yang memiliki `$skill-installer`:

```text
Gunakan $skill-installer untuk memasang skill dari repositori
https://github.com/MaulanaR/mrlabs-reels-generators
pada ref master, path root (.), dengan nama lokal mrlabs-reels-generator.

Periksa watch dan dependensi editor yang saya pilih.
Jika belum tersedia, pasang dari sumber upstream yang disebutkan di README.
```

`SKILL.md` berada di root repositori. Cantumkan `--name mrlabs-reels-generator` jika memasang path `.` melalui skrip installer, dan cantumkan `--ref master` karena branch repositori ini adalah `master`.

### Pilihan 2 — skrip installer lokal di PowerShell

Untuk instalasi Codex yang menyediakan installer di `$CODEX_HOME/skills/.system/skill-installer/`:

```powershell
$reelsCodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$reelsInstaller = Join-Path $reelsCodexRoot 'skills\.system\skill-installer\scripts\install-skill-from-github.py'

python $reelsInstaller --repo MaulanaR/mrlabs-reels-generators --ref master --path . --name mrlabs-reels-generator
```

Jika installer tidak tersedia pada lokasi tersebut, gunakan pilihan pertama dan biarkan Codex menemukan installer atau folder skill aktifnya. Installer akan menolak menimpa folder skill yang sudah ada; simpan perubahan lokal sebelum memperbarui instalasi.

Skill tersedia pada giliran berikutnya setelah berhasil dipasang. Jika belum muncul, muat ulang sesi Codex dan pastikan nama folder serta frontmatter-nya `mrlabs-reels-generator`. Lihat juga [panduan skill OpenAI](https://developers.openai.com/codex/skills).

## Dependensi

### Skill pendamping

| Dependensi | Kegunaan | Sumber |
| --- | --- | --- |
| `watch` | Membaca referensi dan meninjau video hasil | [Watch Skill](https://github.com/oxbshw/watch-skill), folder `skills/watch` |
| `higgsfield` | Jalur pilihan Higgsfield Video Editor/Katana; resolve `/use-video-editor` dahulu | Plugin Higgsfield yang terhubung serta plugin editor yang diminta hasil lookup |
| `hyperframes` / `hyperframes-cli` | Jalur pilihan komposisi HTML/GSAP, caption, preview dan render | Plugin HyperFrames atau [Herk Edit Kit](https://github.com/nateherkai/herk-edit-kit), `.agents/skills/hyperframes` dan `.agents/skills/hyperframes-cli` |
| Remotion | Jalur pilihan komposisi React dan render | Runtime/proyek Remotion yang didukung; skill Remotion bila tersedia, atau [dokumentasi resmi](https://www.remotion.dev/docs) |
| `edit-video` (opsional) | Panduan persiapan footage sumber dan sinkronisasi, tanpa mengganti editor atau suara | Herk Edit Kit, `.agents/skills/edit-video` |

Pasang hanya dependensi editor pilihan. Instalasi melalui plugin juga dapat dipakai: agent perlu menemukan lokasi skill dan referensinya yang sebenarnya. `hyperframes:hyperframes` dan skill Higgsfield yang memakai nama plugin dikenali tanpa mengharuskan folder sibling atau path cache tertentu. Panduan persiapan media tidak mengaktifkan pipeline voice lokal.

Contoh pemasangan Watch dan skill jalur HyperFrames dengan installer PowerShell di atas, **hanya untuk skill yang belum terpasang dan editor yang dipilih**:

```powershell
python $reelsInstaller --repo oxbshw/watch-skill --path skills/watch --name watch
python $reelsInstaller --repo nateherkai/herk-edit-kit --path .agents/skills/edit-video .agents/skills/hyperframes .agents/skills/hyperframes-cli
```

### Runtime lokal

Siapkan Git, Python 3.11–3.13 untuk jalur Watch yang didokumentasikan upstream, FFmpeg beserta `ffprobe`, dan browser yang didukung. Jalur Herk/HyperFrames menggunakan Node.js 22 atau lebih baru; Remotion mengikuti kebutuhan versi proyek yang dipakai. Higgsfield mengikuti prasyarat plugin editor hasil `/use-video-editor`. Pilihan editor tidak mengizinkan instalasi model suara lokal. Instruksi upstream tetap menjadi rujukan jika kebutuhan versi berubah.

**Watch engine:** skill `watch` dan engine CLI adalah dua komponen yang perlu disiapkan. Mengikuti [petunjuk upstream](https://github.com/oxbshw/watch-skill#readme), pemasangan dasar untuk kemampuan frame/retrieval adalah:

```sh
python -m pip install "watch-skill[standard]"
watch-skill doctor
```

Tambahan OCR atau transkripsi lokal dipasang hanya jika dibutuhkan. Untuk PC ringan, gunakan caption/transkrip yang tersedia atau timing segmen narasi; jangan memasang model Whisper besar sebagai prasyarat seluruh workflow.

**Herk Edit Kit (opsional untuk jalur HyperFrames):** clone toolkit ke direktori pilihan Anda, lalu siapkan hanya kebutuhan editing sesuai [README upstream](https://github.com/nateherkai/herk-edit-kit#install). Lewati seluruh langkah TTS, voice-model download, atau layanan voice lokal:

```sh
git clone https://github.com/nateherkai/herk-edit-kit.git
cd herk-edit-kit
npm ci
```

Set lokasi toolkit agar agent dapat menemukan utilitas dan referensinya. Jalankan dari direktori `herk-edit-kit` tersebut:

```powershell
$env:HERK_EDIT_KIT_ROOT = (Get-Location).Path
```

Pada macOS/Linux:

```sh
export HERK_EDIT_KIT_ROOT="$PWD"
```

Variabel di atas berlaku untuk proses/sesi terminal tersebut. Agar terlihat oleh Codex, luncurkan Codex dari lingkungan itu, atur variabel pengguna secara persisten, atau beri tahu agent lokasi toolkit di chat. Skill juga dapat menemukan checkout melalui catatan instalasi dependensi; tidak ada path drive milik pembuat yang wajib diikuti.

Perintah utilitas toolkit dijalankan dari root toolkit. Perintah komposisi HyperFrames dijalankan dari folder yang tercatat pada `editing.project_paths.hyperframes` (default baru `10_editing/hyperframes/`). Proyek lama `10_hyperframes/` tetap dapat dipakai. Pastikan runtime render tersedia tanpa menjalankan setup suara lokal. Herk/HyperFrames tidak menjadi prasyarat jalur Higgsfield saja atau Remotion saja.

## Akun, suara, dan aset visual

| Bagian | Jalur yang digunakan |
| --- | --- |
| Audio video asli | Pertahankan rekaman suara dan sinkronisasi sumber; tidak memerlukan TTS |
| Voice-over baru | **Hanya Google AI Studio TTS online**, ketika diminta; melalui API/browser yang sudah login |
| B-roll utama | Footage internet yang relevan, misalnya dari Pexels/Pixabay, dengan sumber dan izin pakai yang jelas |
| B-roll dari gambar | Foto internet yang sesuai dan boleh digunakan, diberi pan/zoom/parallax saat editing |
| Gambar orisinal jika diperlukan | Imagegen bawaan agent, hanya saat pencarian tidak memenuhi adegan atau dibutuhkan visual khusus |
| SFX | Mixkit sebagai sumber utama; Pixabay sebagai cadangan |
| Editing | Pilihan pengguna: Higgsfield, HyperFrames, Remotion, kombinasi dua, atau ketiganya |

### Google AI Studio TTS

Untuk API, sediakan `GEMINI_API_KEY` melalui environment atau secret store yang dapat diakses agent. Ikuti [panduan key Google](https://ai.google.dev/gemini-api/docs/api-key). Jangan masukkan key ke prompt, chat publik, `production.json`, atau Git. Skill tidak otomatis memuat sebuah `.env` hanya karena file itu ada.

Jika key belum tersedia, agent dapat menggunakan [Google AI Studio](https://aistudio.google.com/) melalui browser, asalkan sesi sudah login dan tool browser mendukung operasi serta pengunduhan hasil. Pengguna mungkin perlu menyelesaikan login sendiri. Tanpa key maupun akses browser yang sesuai, produksi suara berhenti sampai akses tersedia.

Narasi membacakan teks yang sudah disetujui. Arahan nada/tempo disimpan terpisah dari teks yang diucapkan. Model dan voice dipilih dari yang benar-benar tersedia saat produksi. Lihat [panduan TTS skill](references/google-ai-studio-tts.md), [dokumentasi Google](https://ai.google.dev/gemini-api/docs/speech-generation), dan [harga/akses gratis](https://ai.google.dev/gemini-api/docs/pricing).

TTS baru memakai akses **free-only**. Jika akses/kuota tidak tersedia, simpan progres tanpa mengaktifkan billing, berpindah penyedia, atau memakai sintesis lokal. Ini tidak menghalangi edit video yang hanya membutuhkan audio rekaman aslinya. Pada proyek lama, rekaman sumber tetap dapat digunakan; take yang dibuat dengan sintesis lokal/tidak diketahui tidak boleh dilabeli Google TTS. B-roll mengutamakan aset internet gratis; imagegen hanya jika diperlukan. Flow/Gemini untuk pembuatan gambar/video tidak menjadi langkah otomatis.

### Pilih editor video

| Pilihan | Cara dipakai |
| --- | --- |
| **Higgsfield** | Gunakan Video Editor/Katana melalui lookup `/use-video-editor` dan plugin editor yang didukung. |
| **HyperFrames** | Bangun motion graphics, B-roll, caption, transisi, dan assembly dalam komposisi HTML/GSAP. |
| **Remotion** | Bangun adegan, caption, dan assembly dengan komposisi React sesuai runtime yang tersedia. |
| **Gabungan** | Pilih pasangan tertentu atau semua tiga tool; tetapkan tugas masing-masing dan satu editor untuk export final. |

Jika editor belum disebutkan, agent menanyakan pilihan tersebut sambil tetap menyusun naskah. Produksi menunggu persetujuan naskah **dan** pilihan editor. Gaya 01–15 tidak otomatis menentukan editor; agent tidak diam-diam kembali ke HyperFrames.

Contoh gabungan ketiganya: **Higgsfield untuk susunan footage → HyperFrames untuk insert grafis → Remotion untuk assembly, caption, dan mixing final**. Pembagian dapat disesuaikan dengan kebutuhan dan kemampuan tool yang tersedia. Antar-editor memakai file media hasil export yang sudah diperiksa, bukan mengasumsikan format proyek bisa saling dibuka. Caption dan narasi final dipasang satu kali agar tidak berulang. Setiap tahap tetap menyimpan source yang dapat diedit.

Memilih Higgsfield untuk editing tidak otomatis memanggil preset pembuat video/voice, memakai kredit, atau membeli layanan. Jika plugin editor, runtime, fitur, atau jalur export belum tersedia, agent menjelaskan kendalanya dan menawarkan pilihan yang didukung sebelum mengganti jalur. Lihat [panduan editor dan handoff](references/editing-options.md).

### B-roll dari internet dahulu

Agent menggunakan aset milik pengguna yang cocok jika tersedia, lalu mencari [Pexels](https://www.pexels.com/videos/), [Pixabay](https://pixabay.com/videos/), atau sumber lain yang izin pakainya dapat diverifikasi. Kandidat harus sesuai dengan subjek, aksi, setting, crop, dan batasan orang pada naskah; sekadar warna yang mirip belum cukup.

Setelah persetujuan naskah, hanya aset terpilih yang diunduh ke `07_broll_assets/`. URL halaman asal, pembuat bila tersedia, lisensi, kebutuhan atribusi, dan properti media dicatat. Ikuti [lisensi Pexels](https://www.pexels.com/license/) atau [lisensi Pixabay](https://pixabay.com/service/license-summary/) serta ketentuan aset yang digunakan.

Jika pencarian terarah belum menemukan aset yang cocok, atau adegan membutuhkan ilustrasi orisinal, agent mencatat `fallback_reason` lalu memakai skill `imagegen` dan tool gambar bawaan untuk **satu gambar adegan yang dibutuhkan**. Hasilnya disimpan ke proyek dan digerakkan di editor pilihan. Jalur bawaan ini tidak meminta OpenAI API key terpisah; jika tool tidak tersedia, agent menyimpan progres dan menjelaskan kendalanya, bukan otomatis beralih ke layanan visual eksternal. Lihat [panduan B-roll internet](references/internet-broll.md).

### Browser

Pencarian/pengunduhan stock memerlukan web/browser tool yang tersedia di lingkungan agent. Narasi lewat browser AI Studio memerlukan sesi yang sudah login. Sebuah tautan website atau skill yang terpasang tidak otomatis menyediakan kendali browser. Gunakan jalur unduhan yang didukung sumber dan simpan progres jika perlu interaksi pengguna atau akses terhenti.

## Pilih salah satu dari 15 gaya

Preview adalah contoh konsep statis dengan tema demo **“Dari ide ke aksi”**. Gaya visualnya dapat dipakai ulang; isi gambar, objek demo, dan teksnya harus diganti sesuai tema serta naskah proyek baru.

![Lima gaya dari referensi](assets/style-board-reference.png)

<details>
<summary>Lihat gaya 06–15</summary>

![Gaya 06 sampai 10](assets/style-board-new-a.png)

![Gaya 11 sampai 15](assets/style-board-new-b.png)

</details>

| Nomor | Gaya | Cocok untuk |
| --- | --- | --- |
| 01 | Light Explainer | Edukasi, konsep, analogi |
| 02 | Dark Editorial | AI, sistem, perbandingan |
| 03 | Dark Workflow | Developer, tutorial, workflow |
| 04 | **Faceless Editorial** | Review/edukasi dengan tipografi, screenshot, dan diagram tanpa orang |
| 05 | Product Metrics | Produk, bisnis, benefit |
| 06 | Swiss Kinetic | Kampanye, pengumuman, tipografi dinamis |
| 07 | Paper Cut Story | Cerita, kreativitas, UMKM |
| 08 | Blueprint Lab | Sains, engineering, cara kerja |
| 09 | Cinematic Noir | Cerita, craft, suasana sinematik |
| 10 | Pastel 3D | Pemula, pendidikan, produk ramah |
| 11 | Comic Pop | Edutainment, fun fact, promo energik |
| 12 | Luxury Minimal | Premium, arsitektur, brand |
| 13 | Retro Terminal | Coding, teknologi retro, sejarah digital |
| 14 | Nature Documentary | Alam, lingkungan, sains, travel |
| 15 | Collage Editorial | Budaya, opini, cerita kreatif |

Untuk galeri interaktif, clone/unduh repositori atau gunakan salinan yang sudah terpasang, lalu buka [assets/style-gallery.html](assets/style-gallery.html) di browser lokal. GitHub menampilkan source HTML; tampilan interaktif dibuka dari file lokal. Nomor, contoh gambar, dan perintah pemakaian tersedia dalam galeri.

Gaya 04 memakai ID internal lama `presenter-editorial` untuk kompatibilitas, tetapi tampil sebagai **Faceless Editorial** dengan aturan tanpa orang. Nama lama tetap dikenali sebagai alias.

## Contoh penggunaan

### Mengedit video asli dengan semua penambahan

```text
Gunakan $mrlabs-reels-generator.
Video asli: D:\video-saya\tutorial-stok.mp4
Pertahankan wajah, suara, dan penjelasan asli.
Tambahkan informasi pendukung, subtitle Bahasa Indonesia,
motion graphics yang menjelaskan ucapan, dan B-roll internet yang relevan.
Editor: gabungan Higgsfield dan HyperFrames.
Tampilkan transkrip dan rencana edit per timecode untuk saya setujui dahulu.
```

Ganti contoh path dengan file Anda atau lampirkan videonya di chat. Agent membaca video tersebut dan menampilkan rencana konkret sebelum mengedit. Permintaan terbatas, misalnya subtitle saja, tidak dipaksa menjadi produksi penuh dengan potongan/B-roll/TTS.

### Memilih gaya otomatis

```text
Gunakan $mrlabs-reels-generator.
Tema: cara pemula mengatur stok toko agar tidak kehabisan barang.
Pilih gaya yang paling sesuai, durasi sekitar 35 detik.
Tampilkan naskah lengkap dan storyboard untuk persetujuan saya dahulu.
```

### Menentukan B-roll dan SFX

```text
Gunakan $mrlabs-reels-generator.
Tema: proses menyiapkan kopi di kedai.
Gaya: 04 Faceless Editorial, Bahasa Indonesia.
Wajib ada B-roll biji kopi, penggilingan, atau penyeduhan tanpa orang/tangan.
Gunakan SFX seperlunya agar narasi jelas.
Buat naskah dan rencana adegan dahulu untuk saya setujui.
```

Setiap video minimal memuat **satu adegan B-roll yang menjelaskan narasi**. Sumber utamanya adalah internet; imagegen menjadi fallback bila memang dibutuhkan. Diagram/card/caption, prompt yang belum diproduksi, atau klip yang tidak muncul di hasil akhir tidak memenuhi syarat. B-roll dari gambar harus mendapat gerakan yang bermakna saat editing. Jika B-roll wajib belum tersedia, video tidak ditandai selesai.

### Memilih atau menggabungkan editor

```text
Gunakan $mrlabs-reels-generator.
Tema: proses menyiapkan kopi di kedai, gaya 04 Faceless Editorial.
Editor: gabungkan Higgsfield, HyperFrames, dan Remotion.
Suara: Google AI Studio TTS online saja.
Usulkan pembagian tugas editor, naskah, dan storyboard untuk saya setujui.
```

Untuk satu editor, ganti baris editor dengan `Editor: Higgsfield.`, `Editor: HyperFrames.`, atau `Editor: Remotion.` Untuk dua editor, sebutkan pasangannya secara langsung. Ketika melanjutkan proyek dengan pilihan yang sudah tercatat dari pengguna, agent tidak menanyakannya kembali.

### Menyetujui atau merevisi

Setelah melihat naskah dan storyboard, pengguna dapat membalas:

```text
Setuju dengan naskah dan rencana adegan versi ini. Lanjutkan produksi.
```

Atau minta revisi bagian tertentu. Perubahan substantif naskah membutuhkan persetujuan versi baru. Perbaikan crop, caption, timing, atau level SFX yang mempertahankan isi yang disetujui dapat dilanjutkan dengan persetujuan yang masih berlaku.

### Melanjutkan proyek

```text
Lanjutkan proyek reels-projects/kopi-untuk-umkm.
Baca production.json dan cek persetujuan naskah serta aset yang sudah ada.
Gunakan kembali hasil yang sudah diterima dan lanjutkan tahap yang belum selesai.
```

## Hasil dan struktur proyek

Default mode tema: Bahasa Indonesia, 1080 × 1920, 30 fps, sekitar 30–40 detik, H.264/AAC. Durasi akhir mengikuti narasi yang diukur. Mode video asli mengikuti durasi/bahasa/framing sumber atau perubahan yang disetujui pengguna.

```text
reels-projects/<tema>/
  production.json
  DESIGN.md
  00_source/       # mode video asli: sumber, metadata, transkrip sumber
  01_research.md
  02_visual-references/
  03_storyboard.md
  04_voiceover_transcript.md
  05_tts_request.json
  06_scene_assets.json
  07_broll_assets/
  08_voiceover/
  09_edit/
    sfx-cues.json
    sfx/
  10_editing/
    higgsfield/   # bila dipilih
    hyperframes/  # bila dipilih
    remotion/     # bila dipilih
    handoffs/     # export antar-editor untuk gabungan
  11_final/
    <tema>_final.mp4
    VERIFY.md
```

`06_scene_assets.json` merupakan rencana lokal semua adegan: motion graphics, query/kandidat B-roll internet, sumber terpilih, dan prompt imagegen jika fallback memang dibutuhkan. File request TTS tidak berisi kredensial. Pada proyek lama, nama `06_flow_prompts.json`/`07_flow_downloads/` dapat dipertahankan sebagai arsip atau path yang sudah tercatat di manifest; nama lama tersebut tidak mengaktifkan kembali Flow.

Manifest schema `1.7` memiliki `workflow_mode` (`theme_to_reel`/`source_video_edit`), identitas/transkrip/EDL sumber di `source_video`, dan pilihan engine/handoff di `editing`. `narration.mode` membedakan `tts`, `source_audio`, dan `none`; sintesis lokal tetap dilarang. Field `files.composition` diisi setelah editor dipilih. Path lama tetap dipertahankan saat melanjutkan proyek.

Untuk video asli, `files.script` menunjuk `04_edit_review.md`: transkrip asli, identitas sumber, potongan dan seluruh rencana tambahan yang disetujui. Checker versi/hash yang sama dipakai tanpa mewajibkan naskah baru. Simpan `09_edit/source-edl.json`, transkrip sumber dan transkrip output secara terpisah. Request TTS tidak dibuat jika tidak ada narasi baru.

Dalam editor pilihan, B-roll diberi klip/sequence nyata, trim sumber, waktu tampil, crop, dan lapisan yang benar. Narasi tetap berjalan; caption diletakkan di atas footage; audio bawaan B-roll dibisukan kecuali ada suara yang sengaja dipilih sebagai cue terpisah. Lihat [panduan editor](references/editing-options.md) dan, untuk tahap HyperFrames, [panduan integrasi B-roll](references/hyperframes-broll.md).

SFX direncanakan berdasarkan aksi/tema, mengikuti karakter gaya, dan dicampur dengan prioritas narasi. Rekomendasi awal 4–8 aksen untuk Reel 30–40 detik dapat dikurangi sesuai kebutuhan. Catatan sumber/lisensi disimpan, dan raw stock yang lisensinya melarang redistribusi tidak dimasukkan ke paket source yang dibagikan. Lihat [sound design](references/sound-design.md).

## Pemeriksa persetujuan naskah

Agent menjalankan pemeriksa berikut sebelum produksi media, menggunakan path instalasi skill dan proyek yang sebenarnya:

```sh
python scripts/check-script-approval.py /path/to/reels-projects/tema
```

Contoh di atas dijalankan dari direktori skill. Dari direktori lain, gunakan path absolut menuju skrip tersebut. Exit `0` berarti status, versi, hash file, dan field bukti persetujuan konsisten; exit `2` memblokir produksi.

Checker ini **tidak mengautentikasi percakapan dan tidak memberi persetujuan sendiri**. Agent wajib mencatat persetujuan pengguna yang benar-benar diberikan setelah naskah ditampilkan, lalu menyimpan versi/hash yang sesuai. Jangan mengisi approval palsu agar lolos pemeriksaan.

Checker hanya memeriksa konsistensi persetujuan artifact di `files.script` (naskah atau paket review edit). Agent juga memeriksa pilihan editor, identitas sumber/EDL, dan audio sesuai mode: rekaman asli atau TTS online. Lulus checker tidak mengizinkan sintesis lokal atau pemilihan editor sendiri.

## Kendala yang sering muncul

| Kondisi | Tindakan |
| --- | --- |
| Skill tidak ditemukan | Pastikan nama folder/frontmatter benar dan muat ulang sesi bila perlu. |
| Skill ada, engine Watch belum ada | Pasang engine beserta extras yang dibutuhkan dan ikuti hasil `watch-skill doctor`. |
| Path toolkit tidak ditemukan pada jalur Herk/HyperFrames | Beri lokasi checkout Herk yang benar atau set `HERK_EDIT_KIT_ROOT` pada lingkungan Codex. |
| Tidak ada API key TTS | Gunakan browser AI Studio yang sudah login bila tool tersedia, atau siapkan key secara aman. |
| Kuota gratis TTS habis | Simpan progres; lanjutkan saat tersedia. Tidak berpindah ke layanan berbayar atau voice lokal. |
| Editor belum dipilih | Tawarkan Higgsfield, HyperFrames, Remotion, atau gabungan; susun naskah sambil menunggu pilihan. |
| Higgsfield editor/plugin belum tersedia | Jelaskan hasil lookup `/use-video-editor` dan kebutuhan setup; jangan mengarang pengganti sandbox/cloud. |
| Remotion/HyperFrames runtime belum tersedia | Jelaskan kebutuhan jalur pilihan; jangan menjalankan editor lain tanpa pilihan pengguna. |
| Tidak ada kendali browser/login | Selesaikan akses yang diperlukan; agent menyimpan state terlebih dahulu. |
| Aset internet tidak sesuai/tidak dapat digunakan | Cari kandidat relevan lain; gunakan imagegen hanya untuk kebutuhan yang belum terpenuhi dan catat alasannya. |
| Tool imagegen fallback tidak tersedia | Gunakan aset sumber lain yang memenuhi adegan atau simpan kendala; tidak otomatis berpindah ke Flow/Gemini. |
| Timestamp kata tidak tersedia | Gunakan timing segmen yang benar-benar diukur; jangan mengarang karaoke per kata. |
| B-roll hanya berupa file yang diunduh | Masukkan media ke komposisi dan periksa intervalnya pada video encode akhir. |
| PC terbatas | Gunakan gambar dengan gerakan sederhana, timing segmen, efek yang ringan, dan jumlah render worker yang sesuai. Rendering lokal tetap memerlukan resource. |

Repo ini belum menyertakan contoh video yang membuktikan satu produksi cloud lengkap dari tema sampai final. Preview gaya adalah gambar konsep; pemeriksaan visual/audio pada hasil produksi sebenarnya tetap diperlukan. Upload atau publikasi video dilakukan hanya jika diminta pengguna.

## Isi repositori dan referensi

- [SKILL.md](SKILL.md): instruksi utama agent.
- [agents/openai.yaml](agents/openai.yaml): metadata tampilan skill.
- [references/](references/): approval, TTS, gaya, B-roll, SFX, dan kontrak produksi.
- [references/editing-options.md](references/editing-options.md): pilihan editor, gabungan, handoff, dan aturan narasi online.
- [references/source-video-edit.md](references/source-video-edit.md): masukan video asli, transkrip, informasi/subtitle/motion/B-roll, dan pemetaan waktu setelah potongan.
- [assets/](assets/): 15 preview gaya, galeri, papan referensi, dan template proyek/cue.
- [scripts/check-script-approval.py](scripts/check-script-approval.py): pemeriksa persetujuan yang hanya membaca state.

Workflow ini menggunakan [Watch Skill](https://github.com/oxbshw/watch-skill), [Herk Edit Kit](https://github.com/nateherkai/herk-edit-kit), Google AI Studio TTS, B-roll dari sumber seperti [Pexels](https://www.pexels.com/videos/)/[Pixabay](https://pixabay.com/videos/), imagegen bawaan bila diperlukan, serta SFX [Mixkit](https://mixkit.co/free-sound-effects/)/[Pixabay](https://pixabay.com/sound-effects/). Dependensi dan raw stock media tidak dibundel di sini. Ikuti lisensi serta syarat masing-masing sumber. Analisis referensi visual dan tautan video asal ada di [visual-direction.md](references/visual-direction.md).
