# UAS_Keamanan_data

**Nama**: Feril Ferdian  
**Tugas**: UAS Praktikum Keamanan Data dan Informasi

## Isi Repository

Repository ini berisi implementasi beberapa metode keamanan data, yaitu:

1. **Caesar Cipher**  
   File: `caesar_cipher.py`
   
2. **Data Encryption Standard (DES)**  
   File: `des.py`

3. **Steganography (Stegano)**  
   File: `steganoo.py`

## Cara Menjalankan

### Prasyarat

Pastikan Anda memiliki Python versi 3.x terinstal di komputer Anda. Jika belum, unduh dan instal Python melalui [situs resmi Python](https://www.python.org/).

### Langkah-langkah

1. **Instalasi Library yang Diperlukan**

   Pastikan untuk menginstal library seperti `pycryptodome`, `tkinter`, `stegano` dan `Pillow` untuk mendukung implementasi DES, steganografi dalam bentuk GUI:
   ```bash
   pip install pycryptodome pillow tkinter stegano
   ```

2. **Menjalankan Program**

   - **Caesar Cipher**  
     Jalankan file `caesar_cipher.py` dengan perintah berikut:
     ```bash
     python caesar_cipher.py
     ```
     Ikuti petunjuk yang ada pada layar untuk mengenkripsi atau mendekripsi teks.

   - **DES Encryption**  
     Jalankan file `des.py` dengan perintah berikut:
     ```bash
     python des.py
     ```
     Jika file GUI telah tersedia, jalankan program untuk melakukan enkripsi dan dekripsi melalui antarmuka grafis.

   - **Steganography**  
     Jalankan file `steganoo.py` dengan perintah berikut:
     ```bash
     python steganoo.py
     ```
     Pastikan file gambar tersedia jika Anda ingin menyembunyikan pesan di dalam gambar atau mengekstraknya.

## Catatan

- Pastikan semua dependensi terinstal sebelum menjalankan program.
- Jika ada masalah atau error saat menjalankan program, periksa kembali prasyarat dan instalasi library.

