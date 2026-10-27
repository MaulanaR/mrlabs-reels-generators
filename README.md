# MRLabs Islamic Content

Skill Codex untuk membuat konten Islami dari tema dengan dalil yang dapat ditelusuri, voice Google, SFX tanpa musik, serta animasi visual HyperFrames dengan prioritas 3D.

**Nama panggilan:** `$mrlabs-islamic-content`. Skill ini merupakan salinan mandiri dari `mrlabs-reels-generator`; skill induk tetap tersedia. Katalog 15 gaya induk tidak digunakan.

## Mulai memakai

```text
Gunakan $mrlabs-islamic-content.
Tema: pentingnya menjaga lisan.
Instagram: @username_anda
Bahasa Indonesia, durasi mengikuti pembahasan.
Tampilkan naskah, dalil, dan storyboard untuk saya setujui dahulu.
```

Ganti handle contoh dengan username sebenarnya. Skill meminta tema/username yang belum ada, mencari dalil, lalu menampilkan naskah lengkap dan rencana visual sebelum produksi. Username tidak diambil dari proyek lama. API key baru diperlukan ketika akan membuat TTS.

## Aturan utama

- Tidak ada wajah manusia/hewan, termasuk pada foto, pantulan, layar, model 3D, thumbnail, transisi dan preview. Tangan, punggung dan siluet tanpa fitur wajah boleh jika sesuai konteks.
- Nabi hanya ditandai cahaya abstrak dengan nama di tengah sebagai teks editable: tidak ada tubuh/siluet/avatar nabi. Cahaya adalah penanda naratif, bukan klaim rupa nabi. Tidak membuat penggambaran Allah.
- Qur'an: catat surah/ayat, terjemahan dan konteks; utamakan [Qur'an Kemenag](https://bimasislam.kemenag.go.id/al-quran). Hadis: catat kitab, nomor/edisi, derajat dan sumber penilainya. Klaim belum terverifikasi tidak diproduksi.
- Bedakan kutipan, terjemahan, tafsir dan penjelasan. Jangan mengarang dialog nabi, pahala tertentu, atau menyebut musibah sebagai azab tanpa dasar. Ilustrasi perkara gaib bukan dokumentasi bentuk sebenarnya.
- Narasi Google membacakan penjelasan/makna Bahasa Indonesia; tidak menghasilkan tilawah AI. Arab yang ditampilkan harus teks terverifikasi dengan RTL/harakat yang benar.
- Tidak ada musik. SFX nonmusik mengikuti kejadian dan menjaga narasi tetap jelas. Audio bawaan footage/template ikut diperiksa.
- Visual dibangun sebagai animasi kontekstual langsung di HyperFrames: objek, lingkungan, diagram, teks editable dan kamera. Tidak ada B-roll, pencarian footage stock, atau kuota klip pendukung. Imagegen hanya opsional untuk tekstur/ilustrasi yang diperlukan adegan yang disetujui.
- Credit penutup: username sebenarnya dan **Like & share jika bermanfaat.** Tidak ada janji pahala untuk engagement.

## Alur dan persetujuan

Tema + username -> riset dalil -> naskah dan storyboard -> persetujuan manusia -> narasi/aset -> HyperFrames -> pemeriksaan encode -> export.

Sebelum persetujuan, riset, pencarian kandidat/lisensi, inspeksi aset yang sudah ada dan drafting diperbolehkan. TTS, pembuatan adegan/download aset dan SFX produksi, imagegen, animatic dan render menunggu persetujuan. Persetujuan berlaku pada versi/hash naskah serta paket dalil/storyboard/desain/kredit yang ditampilkan. Memilih tema bukan menyetujui naskah yang belum dibaca.

Pemeriksa `check-script-approval.py` hasil clone tetap dipakai. `workflow_guard.py` menambahkan pemeriksaan paket persetujuan dan kebijakan skill; keduanya tidak memberikan persetujuan sendiri. Flag pemeriksaan akhir wajib berdasarkan pemeriksaan nyata, bukan diisi agar lolos.

## Latar dan contoh visual baru

Tersedia **18 latar dengan 54 variasi konteks**: Azab Mencekam, Gurun Siang, Masjid Tenang, Kota Keseharian, Rumah Hangat, Sungai Tafakkur, Hutan Hujan, Pegunungan Fajar, Laut Senja, Kebun Subur, Pasar Amanah, Ruang Belajar, Bengkel Kerja, Halaman Hujan, Malam Berbintang, Jalan Persimpangan, Perpustakaan Ilmu, dan Lembah Badai.

Latar dipilih **per adegan sesuai naskah**, bukan satu gambar yang dipakai sepanjang video. Agent memvariasikan area lokasi, objek, pencahayaan dan sudut/pergerakan kamera dengan transisi halus. Jika cerita tetap di satu tempat, variasikan komposisi dan aksi tanpa memaksakan pindah lokasi. Daftar ini dapat diperluas dengan latar khusus yang lebih cocok; tidak semua pembahasan menggunakan gurun/masjid. Waktu, cuaca dan elemen sejarah tetap harus sesuai konteks.

Buka [galeri 18 latar](assets/style-gallery.html) atau papan [01–06](assets/islamic-background-board.png), [07–12](assets/islamic-background-board-02.png), [13–18](assets/islamic-background-board-03.png). Ada satu contoh gambar per profil, sedangkan 54 variasinya berupa arahan konteks untuk produksi. Preview berupa render statis native Three.js WebGL, dengan objek solid, perspektif dan bayangan. Ini belum merupakan video HyperFrames final. Sumber lookdev ada di `assets/background-worlds.html`; runtime Three.js r180 lokal beserta lisensi MIT tersedia dalam `assets/vendor/`. Galeri/PNG dapat dibuka langsung; preview WebGL memerlukan folder skill dilayani melalui HTTP lokal.

## Editor dan motion

HyperFrames merupakan mesin utama; tidak ada pertanyaan wajib memilih editor induk. Gunakan GSAP untuk gerakan halus berdasarkan waktu komposisi. Target utama adalah **dunia 3D berisi objek solid dan lingkungan yang terasa nyata**, seperti [referensi Scroll Engineer](https://www.instagram.com/p/DeOCrrTqbw6/): perspektif, kedalaman, skala, material, cahaya/bayangan, serta gerakan kamera/objek yang menjelaskan narasi. Gayanya 3D sederhana/low-poly, bukan klaim fotorealistik. Diagram, ikon dan teks hanya lapisan pendukung; bukan isi utama di atas latar polos. Three.js membangun adegan, HyperFrames mengatur komposisi, audio, caption dan export. Periksa capture WebGL sebelum render panjang; jika gagal, laporkan hambatan tanpa diam-diam mengganti hasil dengan SVG/slide. [Analisis visual referensi](references/reference-analysis.md).

Subtitle menggunakan panel berkontras baik, border halus, sudut rounded sekitar 24 px pada kanvas 1080 px, maksimal dua baris dan timing audio aktual. Teks Arab, sumber dan subtitle Indonesia punya layer jelas. SFX mengikuti aksi (misalnya angin, air, langkah, pintu, kertas, guruh); suara melodi/musik tidak dipakai.

## Voice Google dan API key

Narasi baru hanya memakai Google AI Studio TTS online. VoiceStudio/Kokoro/backend TTS lokal dan auto-voice editor tidak digunakan. Akses gratis harus benar-benar tersedia; key saja tidak membuktikan kuota gratis. Model, voice dan format respons mengikuti [dokumentasi Google](https://ai.google.dev/gemini-api/docs/speech-generation) saat produksi. Tidak otomatis memakai billing atau provider lain ketika gagal.

Sediakan key **secara lokal**, bukan di chat:

1. Buat folder `.secrets` di folder skill ini, lalu salin `.env.example` menjadi `.secrets/google-tts.env`.
2. Isi nilai `GEMINI_API_KEY` di file privat tersebut melalui editor lokal.
3. Jika tidak menggunakan file, konfigurasi environment `GEMINI_API_KEY` atau `GOOGLE_API_KEY` yang dapat diakses Codex.

Prioritas: file privat skill -> `GEMINI_API_KEY` -> `GOOGLE_API_KEY`. Key tidak disalin dari skill induk. File privat, `.env`, kredensial dan secret tidak boleh masuk Git, prompt, request JSON atau log. Helper memilih key secara eksplisit agar precedence SDK tidak mengganti sumber terpilih.

```sh
python scripts/google_tts_credentials.py --status
```

Perintah dari folder skill tersebut hanya menampilkan status/sumber key tanpa nilainya; tidak menguji akses API/kuota. Untuk pemakaian programatik, impor `resolve_key()` dari helper dan kirim nilainya langsung ke client Google, tanpa mencetak/log nilainya. Helper tidak menjalankan file `.env` sebagai kode. Jika key belum ada, agent meminta pengguna menyiapkan file/input rahasia saat TTS diperlukan.

## Durasi dan hasil

Output utama 1080 x 1920 (9:16), 30 fps, MP4 H.264/AAC. Durasi mengikuti pembahasan dan audio aktual termasuk penutup, bisa lebih dari satu menit tanpa pemotongan otomatis.

YouTube Shorts maksimal tiga menit menurut [panduan YouTube](https://support.google.com/youtube/answer/15424877?hl=en). Jika lebih panjang, tetap hasilkan master utuh dan klasifikasikan sebagai video vertikal biasa; tidak otomatis dijadikan seri. Batas Instagram diperiksa sesuai jalur publikasi aktual. Status belum terverifikasi dicatat tanpa mengubah master atau menjanjikan kelayakan upload.

Hasil: MP4, subtitle SRT/VTT, timing audio, proyek editable, naskah/storyboard yang disetujui, daftar dalil, sumber/lisensi aset dan `VERIFY.md` berisi apa yang benar-benar diperiksa. Upload/publikasi tidak otomatis.

## Proyek

```text
islamic-projects/<tema>/
  production.json
  DESIGN.md
  01_research.md
  01_religious_references.json
  02_visual-references/
  03_storyboard.md
  04_voiceover_transcript.md
  05_review_package.json
  05_tts_request.json       # hanya ketika membuat narasi baru
  06_scene_assets.json
  07_scene_assets/
  08_voiceover/
  09_edit/sfx-cues.json
  10_editing/hyperframes/
  11_final/<tema>_final.mp4
  11_final/VERIFY.md
```

Template schema `1.9` berfokus pada animasi HyperFrames, tanpa field minimum B-roll. Field kebijakan Islami, sumber dalil, kredit, motion 3D, caption, paket review dan status platform tetap digunakan. Proyek lama mengikuti catatan migrasi di kontrak produksi; jangan memalsukan atau memakai ulang hash persetujuan setelah rencana visual berubah. Jalur secret relatif terhadap **folder skill**, bukan folder proyek; path media relatif terhadap proyek.

```sh
python <folder-skill>/scripts/workflow_guard.py <folder-proyek> --digest
python <folder-skill>/scripts/workflow_guard.py <folder-proyek>
python <folder-skill>/scripts/workflow_guard.py <folder-proyek> --final
```

`--digest` hanya menghitung hash paket review untuk dicatat setelah persetujuan asli. Mode biasa memeriksa syarat produksi; `--final` juga memeriksa catatan penerimaan hasil. Tidak ada opsi auto-approve. Baca [kontrak produksi](references/production-contract.md) untuk field yang harus berasal dari pekerjaan/bukti sebenarnya.

## Video asli opsional

Jika nanti pengguna secara eksplisit memberikan video untuk diedit, gunakan mode `source_video_edit`: pertahankan sumber, transkrip dan audio rekaman yang sesuai kebijakan. Larangan wajah/musik tetap berlaku; crop, ganti bagian atau hilangkan sumber terlarang melalui rencana yang disetujui. Jangan mengaku musik sudah dihilangkan jika hasilnya belum diperiksa. Audio asli bukan sintesis lokal dan tidak memerlukan Google TTS. Lihat [panduan sumber](references/source-video-edit.md).

## Pemasangan dan dependensi

Skill ini berada sementara di branch **`mrlabs-islamic-content`**, pada root repositori [mrlabs-reels-generators](https://github.com/MaulanaR/mrlabs-reels-generators/tree/mrlabs-islamic-content). Branch `master` berisi skill induk.

Minta Codex yang memiliki `$skill-installer` memasang versi yang tepat:

```text
Gunakan $skill-installer untuk memasang skill dari
https://github.com/MaulanaR/mrlabs-reels-generators
ref mrlabs-islamic-content, path root (.),
dengan nama lokal mrlabs-islamic-content.
```

Jika menggunakan skrip installer secara langsung:

```sh
python /path/to/skill-installer/scripts/install-skill-from-github.py --repo MaulanaR/mrlabs-reels-generators --ref mrlabs-islamic-content --path . --name mrlabs-islamic-content
```

Ganti path installer dengan lokasi yang sebenarnya. Jangan menghilangkan `--ref`: branch default memasang skill induk. Alternatifnya salin folder skill dari branch ini ke folder skills Codex yang aktif. Installer menolak menimpa instalasi yang ada; simpan perubahan lokal sebelum memperbarui. Skill tersedia pada giliran berikutnya; jika belum muncul, muat ulang sesi dan pastikan nama folder/frontmatter sama.

Dependensi editing: HyperFrames dan CLI, GSAP, Node/browser yang didukung, FFmpeg/ffprobe. Watch digunakan untuk inspeksi sumber/hasil. Tool web diperlukan untuk riset dan sumber/lisensi. Imagegen bawaan opsional, bukan syarat seluruh proyek. Resolve skill/plugin dari lokasi instalasi sebenarnya. Jangan memasang model speech berat atau menjalankan setup voice lokal.

Jika menggunakan Herk helpers, gunakan `HERK_EDIT_KIT_ROOT` atau checkout yang benar; toolkit tidak dibundel. Key Google, sumber pribadi, footage/suara stock, node_modules dan cache tidak ikut paket skill. Hormati lisensi redistribusi aset: berikan hasil mix dan catatan sumber bila raw stock tidak boleh dibagikan.

Pemeriksaan template/guard atau preview statis tidak membuktikan sebuah produksi video selesai. Laporan harus membedakan validasi lokal, akses Google yang benar-benar diuji, review visual/listening dan hasil encode. Skill induk dan branch `master` tetap dipertahankan; perubahan ini hanya ada pada branch `mrlabs-islamic-content`.
