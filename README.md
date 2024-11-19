Grote Cellular Management System
Sistem manajemen toko Grote Cellular dirancang untuk mengelola data smartphone, termasuk melihat daftar, menambahkan, menghapus, memperbarui, membeli smartphone, dan fitur sorting. Program ini memiliki dua jenis akses: Admin dan User.

Fitur
**Admin**

-Melihat Daftar Smartphone: Menampilkan semua data smartphone.
-Menambahkan Smartphone: Menambahkan smartphone baru ke daftar.
-Menghapus Smartphone: Menghapus smartphone dari daftar.
-Mengupdate Smartphone: Memperbarui data (nama, stok, harga, merek) smartphone.
-Fitur Sorting: Mengurutkan smartphone berdasarkan kolom (Nama, Stok, Harga, Merek) secara ASC/DESC.

**User**

-Melihat Daftar Smartphone: Melihat semua smartphone yang tersedia.
-Melihat Detail Smartphone: Informasi detail tentang smartphone tertentu.
-Membeli Smartphone: Menambahkan smartphone ke keranjang dan mencetak struk belanja.
-Fitur Sorting: Sama seperti admin.

Alur Program
1. Login:
2. Pilih peran: Admin (1) atau User (2).
3. Admin harus memasukkan password (admin).

Admin Menu:
1. Pilih opsi yang diinginkan:
2 Lihat daftar smartphone.
3 Tambah/hapus/update smartphone.
4 Sorting data smartphone.
5 Keluar program.

User Menu:
1. Pilih opsi yang diinginkan:
2. Lihat daftar smartphone.
3. Lihat detail smartphone.
4. Beli smartphone.
5. Keluar program.
6. Konfirmasi & Navigasi:

Setiap perubahan (tambah/hapus/update) memerlukan konfirmasi.
Program akan kembali ke menu utama setelah selesai menjalankan fungsi.

Teknologi & Library
Python
maskpass: Untuk keamanan input password.
tabulate: Menampilkan data dalam bentuk tabel.
datetime: Untuk mencetak waktu pada struk belanja.

Cara Menjalankan
Pastikan semua library yang dibutuhkan telah terinstal (pip install maskpass tabulate).
Jalankan file Python menggunakan terminal atau IDE.
Ikuti panduan login dan pilih fitur yang diinginkan.
