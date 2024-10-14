# Mini-Projet-2-DP
Nama : Fauzia Inanta Aurelia | NIM : 2409116044 | Sistem Informasi'B
# Tema : Penyewaan Kursi Lipat

# 1. Flowchart
![minpro 2 drawio (1)](https://github.com/user-attachments/assets/21a12d1a-fbcd-465e-a3c0-88d5faae4678)

# 2. Penjelasan Kode
1. Menampilkan Header
Di awal program, ditampilkan dua pesan sambutan sebagai informasi untuk pengguna.
![image](https://github.com/user-attachments/assets/ac2f1bc9-89d9-4d73-81b7-3230dba6e2d2)
Ini hanya bertujuan untuk memperkenalkan program kepada pengguna saat mereka menjalankan aplikasi

2. Mengimpor Library
Mengimpor library PrettyTable yang digunakan untuk menampilkan data kursi dalam bentuk tabel yang rapi.
![image](https://github.com/user-attachments/assets/b3dd24c4-43ab-46f5-907c-fe1acc29f957)

3. Inisialisasi Data
Di sini, kita membuat tiga variabel utama untuk menyimpan data.
![image](https://github.com/user-attachments/assets/0fc3ff23-afdf-4bc5-abc5-6ff44d06e5d3)
pengguna: List berisi data akun. Pada awalnya, hanya terdapat satu pengguna, yaitu admin ('fauzia admin'), yang sudah terdaftar.

kursi: List kosong yang akan diisi dengan data kursi. Setiap kursi diwakili sebagai dictionary dengan atribut: nama, jumlah, dan harga.

transaksi: List untuk menyimpan detail transaksi pemesanan kursi, berisi informasi seperti nama kursi, jumlah yang dipesan, durasi sewa, dan total harga.

4. Fungsi CRUD dan Transaksi Kursi
lihat_kursi(): Fungsi ini menampilkan daftar kursi dalam bentuk tabel menggunakan PrettyTable.

Proses:

Mengecek apakah list kursi kosong.
Jika ada kursi, menampilkan semua data kursi dalam tabel.
![image](https://github.com/user-attachments/assets/57e2cfc8-6b66-4104-809e-814359de0dd0)
tambah_kursi(nama, jumlah, harga): Admin dapat menambah kursi baru dengan memberikan nama, jumlah, dan harga sewa per hari.

Proses:

Menambahkan dictionary kursi baru ke dalam list kursi.
Menampilkan pesan bahwa kursi berhasil ditambahkan
![image](https://github.com/user-attachments/assets/7ac931a6-3ebd-49ab-9ebc-9faae44d9722)
hapus_kursi(nama): Admin dapat menghapus kursi dari list kursi berdasarkan nama kursi.

Proses:

Mencari kursi berdasarkan nama.
Jika ditemukan, kursi dihapus dari list dan menampilkan pesan sukses.
Jika tidak ditemukan, menampilkan pesan bahwa kursi tidak ditemukan.
![image](https://github.com/user-attachments/assets/40eb88be-39f8-4665-80c8-2e090e8fb2e1)
pesan_kursi(nama, jumlah, jumlah_hari): User bisa memesan kursi yang tersedia.

Proses:

Mencari kursi yang ingin dipesan berdasarkan nama.
Mengecek apakah jumlah kursi yang tersedia cukup.
Jika cukup, mengurangi jumlah kursi di stok dan menambahkan transaksi ke list transaksi.
Menghitung total harga sewa berdasarkan jumlah kursi dan lama penyewaan.
Jika kursi tidak cukup, memberi pesan peringatan.
![image](https://github.com/user-attachments/assets/04565e00-79ef-412e-8dc4-9df508cde185)
kembalikan_kursi(nama, jumlah): User bisa mengembalikan kursi yang telah disewa.

Proses:

Mencari transaksi yang sesuai dengan kursi yang ingin dikembalikan.
Jika transaksi ditemukan dan jumlah kursi valid, kursi ditambahkan kembali ke stok.
Jika data tidak valid (misalnya jumlah kursi melebihi yang dipesan), memberi peringatan bahwa pengembalian gagal.
![image](https://github.com/user-attachments/assets/99a4abf9-e49e-46bf-b1a7-651f5549dc27)










