# UAS_Keamanan_data
# README

**Nama**: Feril Ferdian  
**Tugas**: UAS Praktikum Keamanan Data dan Informasi

## Isi Repository

Repository ini berisi implementasi beberapa metode keamanan data, yaitu:

1. **Caesar Cipher**  
   File: `caesar_cipher.py`
   
2. **Data Encryption Standard (DES)**  
   File: `des_encryption.py`

3. **Steganography (Stegano)**  
   File: `steganography.py`

## Cara Menjalankan

### Prasyarat

Pastikan Anda memiliki Python versi 3.x terinstal di komputer Anda. Jika belum, unduh dan instal Python melalui [situs resmi Python](https://www.python.org/).

### Langkah-langkah

1. **Clone Repository**

   Clone repository ini ke dalam komputer Anda:
   ```bash
   git clone https://github.com/username/keamanan-data-informasi.git
   cd keamanan-data-informasi
   ```

2. **Instalasi Library yang Diperlukan**

   Beberapa file mungkin memerlukan library tambahan. Anda dapat menginstalnya dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```

   Jika file `requirements.txt` belum ada, pastikan untuk menginstal library seperti `pycryptodome` dan `Pillow` untuk mendukung implementasi DES dan steganografi:
   ```bash
   pip install pycryptodome pillow
   ```

3. **Menjalankan Program**

   - **Caesar Cipher**  
     Jalankan file `caesar_cipher.py` dengan perintah berikut:
     ```bash
     python caesar_cipher.py
     ```
     Ikuti petunjuk yang ada pada layar untuk mengenkripsi atau mendekripsi teks.

   - **DES Encryption**  
     Jalankan file `des_encryption.py` dengan perintah berikut:
     ```bash
     python des_encryption.py
     ```
     Jika file GUI telah tersedia, jalankan program untuk melakukan enkripsi dan dekripsi melalui antarmuka grafis.

   - **Steganography**  
     Jalankan file `steganography.py` dengan perintah berikut:
     ```bash
     python steganography.py
     ```
     Pastikan file gambar tersedia jika Anda ingin menyembunyikan pesan di dalam gambar atau mengekstraknya.

## Catatan

- Pastikan semua dependensi terinstal sebelum menjalankan program.
- Jika ada masalah atau error saat menjalankan program, periksa kembali prasyarat dan instalasi library.

---

Dibuat oleh Feril Ferdian untuk keperluan tugas UAS Praktikum Keamanan Data dan Informasi.

