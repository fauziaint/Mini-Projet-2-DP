# Mini-Projet-2-DP
Nama : Fauzia Inanta Aurelia | NIM : 2409116044 | Sistem Informasi'B
# Tema : Penyewaan Kursi Lipat

# 1. Flowchart
![minpro 2 drawio (1)](https://github.com/user-attachments/assets/21a12d1a-fbcd-465e-a3c0-88d5faae4678)

# 2. Penjelasan Kode
- Program dimulai dengan menampilkan pesan pembuka dan mengimpor modul PrettyTable untuk menampilkan tabel kursi.
  
![Screenshot 2024-10-14 221255](https://github.com/user-attachments/assets/6623ece8-5df1-4fa7-891a-705c159a5d3a)

- pengguna : List ini menyimpan data pengguna. Admin sudah terdaftar secara default dengan username admin dan password admin123.
-  kursi : List ini menyimpan data kursi yang tersedia untuk disewa.
-  transaksi : List ini menyimpan data transaksi penyewaan kursi.

Fungsi Lihat, Tambah, Hapus, Pesan, dan Kembalikan Kursi

- lihat kursi() : Menampilkan daftar kursi yang tersedia dalam bentuk tabel. Jika tidak ada kursi, akan mencetak pesan bahwa kursi tidak tersedia.
  
![Screenshot 2024-10-14 193019](https://github.com/user-attachments/assets/01798e84-1c56-4ff1-95f4-a54b2308fcfb)

- tambah kursi(nama, jumlah, harga) : Fungsi ini digunakan oleh admin untuk menambahkan kursi baru ke daftar.
- 
![Screenshot 2024-10-14 160126](https://github.com/user-attachments/assets/b1d332c4-e1be-4cb3-a1d2-0ae0bad71343)

- hapus kursi(nama) : Admin bisa menghapus kursi dari daftar berdasarkan nama kursi.
  
![Screenshot 2024-10-14 160134](https://github.com/user-attachments/assets/e8e251f9-8f3d-4b74-b0d3-d94ddf73fe92)

- pesan kursi(nama, jumlah, jumlah_hari) : Fungsi ini memungkinkan user untuk memesan kursi dengan jumlah dan lama penyewaan tertentu. Jika jumlah kursi mencukupi, pesanan akan diproses.

![Screenshot 2024-10-14 160134](https://github.com/user-attachments/assets/e8e251f9-8f3d-4b74-b0d3-d94ddf73fe92)

- kembalikan kursi(nama, jumlah) : User bisa mengembalikan kursi yang sudah disewa dengan mengurangi jumlah kursi yang dipinjam dan menambahkannya kembali ke stok.

![Screenshot 2024-10-14 160144](https://github.com/user-attachments/assets/fb4570c4-6992-4b0a-8ad3-a79010913aed)

Fungsi Register dan Login

- register(username, password) : Fungsi ini digunakan untuk mendaftarkan user baru dengan username dan password.
-  login(username, password) : Memeriksa apakah username dan password yang dimasukkan sesuai dengan yang terdaftar. Mengembalikan role (admin/user) jika berhasil, atau None jika gagal.


![Screenshot 2024-10-14 160310](https://github.com/user-attachments/assets/b1e74356-7029-4f50-a2c5-92d7e5dae57c)


![Screenshot 2024-10-14 185357](https://github.com/user-attachments/assets/6051bf94-0e78-410d-9801-77243cf4224d)
![Screenshot 2024-10-14 185532](https://github.com/user-attachments/assets/870656dd-d0b7-40e7-bc88-0d355c5b5026)
![Screenshot 2024-10-14 185604](https://github.com/user-attachments/assets/01258d33-4ff9-470a-8cc1-6dbb96fb257e)
![Screenshot 2024-10-14 185625](https://github.com/user-attachments/assets/afac4d7b-1c13-4ad9-b0b3-d733a0d97c00)
![Screenshot 2024-10-14 185635](https://github.com/user-attachments/assets/5cf1b03c-6be6-41cf-a539-c535dac5f77b)




