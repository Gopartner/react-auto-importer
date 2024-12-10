# **React Auto Importer**

**React Auto Importer** adalah skrip Python yang secara otomatis mendeteksi komponen React yang digunakan dalam kode dan menambahkan pernyataan impor yang sesuai. Skrip ini dibuat untuk digunakan dengan editor **Vim** dan membantu meningkatkan produktivitas pengembangan dengan menghilangkan kebutuhan untuk menulis impor secara manual.

## **Fitur Utama**

- **Pencarian Otomatis Komponen**: Mendeteksi komponen React dalam file dan mencari lokasinya di dalam direktori `src` dan subdirektorinya.
- **Penambahan Impor Otomatis**: Menambahkan pernyataan `import` untuk komponen yang terdeteksi.
- **Penanganan Komponen Tidak Ditemukan**: Menambahkan komentar jika komponen tidak ditemukan sebagai pengingat untuk meninjau impor.
- **Menghindari Duplikasi**: Tidak menambahkan impor atau komentar yang sudah ada.
- **Dukungan Dinamis**: Bekerja di berbagai proyek React tanpa konfigurasi tambahan.

## **Prasyarat**

Pastikan sistem Anda sudah terinstal:

- **Python 3**
- **Vim Editor**
- Proyek React dengan struktur direktori yang memiliki folder `src`

## **Instalasi**

1. **Clone repository ini**:

   ```bash
   git clone https://github.com/Gopartner/react-auto-importer.git

2. **Atur konfigurasi Vim di .vimrc atau init.vim dengan menambahkan baris berikut:
   ```bash
   autocmd BufWritePost *.js,*.jsx !python3 ~/react-auto-importer/auto_import_react.py %:p

Penjelasan:

autocmd: Perintah otomatis untuk Vim.

BufWritePost: Event yang dipicu setelah file disimpan.

*.js,*.jsx: Pola file yang ingin diawasi (file JavaScript dan JSX).

!python3 ~/react-auto-importer/auto_import_react.py %:p: Menjalankan skrip Python dengan path lengkap file (%:p) yang sedang diedit.
