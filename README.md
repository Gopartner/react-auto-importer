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


