# ModeBrutal — WordPress Brute Force Tool

🚀 **Aggressive WordPress Login Cracker**  
By **X'Boy Linux** | Tool Project: `ModeBrutal`

> Dibuat untuk red teaming, bug bounty, atau CTF — gunakan hanya untuk tujuan legal & edukatif.

---

## 🧠 Fitur Utama

- 🚀 Multi-threaded (default 50 threads, super cepat)
- 🧑‍💻 Dukungan username default (`admin`)
- 🎯 Deteksi otomatis WordPress (`wp-login.php`)
- 📥 Hasil login valid disimpan di `valid.txt`
- ⚡ Mode agresif (tanpa delay, brute terus)
- 🌈 Tampilan terminal berwarna + ASCII banner
- 🔧 Bypass dan pengecekan otomatis
- 🛡️ Bisa edit manual untuk Proxy & Telegram bot

---

## 📦 Instalasi

```bash
# Clone dari GitHub
git clone https://github.com/ModeBrutal/Wp-Brute
cd Wp-Brute

# Install Python dependency
pip install requests colorama
```

---

## 🕹️ Cara Pakai

```bash
python wp.py
```

Akan muncul prompt input:

- File daftar target: `site.txt`
- File password list: `pass.txt`

> Tool akan otomatis mendeteksi WordPress, melewati yang bukan, dan brute force login form `wp-login.php`.

---

## 📤 Output

- ✅ Login sukses otomatis disimpan ke: `valid.txt`
- 🤖 Jika Telegram diaktifkan, hasil dikirim otomatis ke bot

---

## 🔧 Konfigurasi Opsional (Telegram)

Untuk mengirim notifikasi ke Telegram:

Edit bagian di awal script `wp.py`:

```python
TOKEN = "ISI_TOKEN_BOT_KAMU"
CHAT_ID = "ISI_CHAT_ID_KAMU"
```

> Pastikan kamu sudah mulai chat dengan bot tersebut agar bisa menerima notifikasi.

---

## 📘 Contoh Output Terminal

```
𝙈𝙤𝙙𝙚𝘽𝙧𝙪𝙩𝙖𝙡 - 𝙒𝙤𝙧𝙙𝙥𝙧𝙚𝙨𝙨 𝘽𝙧𝙪𝙩𝙚 𝙏𝙤𝙤𝙡
   Status: Ready         Threads: 50
   Mode: Aggressive      Proxy: off
   Result: valid.txt     Bypass: Enabled
   Team: ......   Dev: X'Boy Linux
```

---

## ❗ Catatan

- Tool ini **tidak menyerang** WordPress.com (`*.wordpress.com`)
- Hanya untuk self-hosted WordPress (yang punya akses `wp-login.php`)
- Gunakan wordlist yang realistis dan umum

---

## ⚠️ Disclaimer

Tool ini dibuat hanya untuk:
- 🧪 Riset keamanan
- 🎓 Pembelajaran pribadi
- 🕹️ CTF atau challenge legal

🛑 Dilarang digunakan untuk aktivitas ilegal atau tanpa izin.  
Pengembang **tidak bertanggung jawab atas penyalahgunaan**.

---

## 📫 Kontak & Kredit

- 💀 Developer: X'Boy Linux
- 🔗 GitHub: [github.com/ModeBrutal](https://github.com/ModeBrutal)
- ✉️ Telegram: [@xboylinux](https://t.me/xboylinux)

---

## ⭐ Dukungan

Bantu proyek ini berkembang:  
🌟 Star repo ini | 🔁 Share ke sesama researcher | 💬 Kirim feedback ke Telegram

---

© 2025 ModeBrutal — All rights reserved.
