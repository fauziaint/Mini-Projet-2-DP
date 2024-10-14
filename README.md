# Mini-Projet-2-DP
Nama : Fauzia Inanta Aurelia | NIM : 2409116044 | Sistem Informasi'B
# Tema : Penyewaan Kursi Lipat

# 1. Flowchart
![minpro 2 drawio (1)](https://github.com/user-attachments/assets/21a12d1a-fbcd-465e-a3c0-88d5faae4678)

# 2. Penjelasan Kode
- Menampilkan Header
Di awal program, ditampilkan dua pesan sambutan sebagai informasi untuk pengguna.
![image](https://github.com/user-attachments/assets/ac2f1bc9-89d9-4d73-81b7-3230dba6e2d2)
Ini hanya bertujuan untuk memperkenalkan program kepada pengguna saat mereka menjalankan aplikasi

- Mengimpor Library
Mengimpor library PrettyTable yang digunakan untuk menampilkan data kursi dalam bentuk tabel yang rapi.

![image](https://github.com/user-attachments/assets/b3dd24c4-43ab-46f5-907c-fe1acc29f957)

- Inisialisasi Data
Di sini, kita membuat tiga variabel utama untuk menyimpan data.

![image](https://github.com/user-attachments/assets/0fc3ff23-afdf-4bc5-abc5-6ff44d06e5d3)

pengguna: List berisi data akun. Pada awalnya, hanya terdapat satu pengguna, yaitu admin ('fauzia admin'), yang sudah terdaftar.

kursi: List kosong yang akan diisi dengan data kursi. Setiap kursi diwakili sebagai dictionary dengan atribut: nama, jumlah, dan harga.

transaksi: List untuk menyimpan detail transaksi pemesanan kursi, berisi informasi seperti nama kursi, jumlah yang dipesan, durasi sewa, dan total harga.

-  Fungsi CRUD dan Transaksi Kursi
lihat_kursi(): Fungsi ini menampilkan daftar kursi dalam bentuk tabel menggunakan PrettyTable.

Proses:

- Mengecek apakah list kursi kosong.
Jika ada kursi, menampilkan semua data kursi dalam tabel.

![image](https://github.com/user-attachments/assets/57e2cfc8-6b66-4104-809e-814359de0dd0)

- tambah_kursi(nama, jumlah, harga): Admin dapat menambah kursi baru dengan memberikan nama, jumlah, dan harga sewa per hari.

Proses:

Menambahkan dictionary kursi baru ke dalam list kursi.
Menampilkan pesan bahwa kursi berhasil ditambahkan

![image](https://github.com/user-attachments/assets/7ac931a6-3ebd-49ab-9ebc-9faae44d9722)

- hapus_kursi(nama): Admin dapat menghapus kursi dari list kursi berdasarkan nama kursi.

Proses:

Mencari kursi berdasarkan nama.
Jika ditemukan, kursi dihapus dari list dan menampilkan pesan sukses.
Jika tidak ditemukan, menampilkan pesan bahwa kursi tidak ditemukan.

![image](https://github.com/user-attachments/assets/40eb88be-39f8-4665-80c8-2e090e8fb2e1)

- pesan_kursi(nama, jumlah, jumlah_hari): User bisa memesan kursi yang tersedia.

Proses:

Mencari kursi yang ingin dipesan berdasarkan nama.
Mengecek apakah jumlah kursi yang tersedia cukup.
Jika cukup, mengurangi jumlah kursi di stok dan menambahkan transaksi ke list transaksi.
Menghitung total harga sewa berdasarkan jumlah kursi dan lama penyewaan.
Jika kursi tidak cukup, memberi pesan peringatan.

![image](https://github.com/user-attachments/assets/04565e00-79ef-412e-8dc4-9df508cde185)

- kembalikan_kursi(nama, jumlah): User bisa mengembalikan kursi yang telah disewa.

Proses:

Mencari transaksi yang sesuai dengan kursi yang ingin dikembalikan.
Jika transaksi ditemukan dan jumlah kursi valid, kursi ditambahkan kembali ke stok.
Jika data tidak valid (misalnya jumlah kursi melebihi yang dipesan), memberi peringatan bahwa pengembalian gagal.
![image](https://github.com/user-attachments/assets/99a4abf9-e49e-46bf-b1a7-651f5549dc27)

- Fungsi Pengguna: Register dan Login
register(username, password): Fungsi ini mendaftarkan pengguna baru sebagai "user".

Proses:

Membuat dictionary baru berisi username, password, dan peran ('user'), lalu menambahkannya ke list pengguna.
![image](https://github.com/user-attachments/assets/d7ed5170-5d01-48b6-b19c-d9c2a56c4e0f)

- login(username, password): Fungsi untuk memverifikasi login berdasarkan username dan password.

Proses:

Membandingkan username dan password yang dimasukkan dengan yang ada di list pengguna.
Jika cocok, mengembalikan peran pengguna (admin atau user).
Jika tidak cocok, mengembalikan None.
![image](https://github.com/user-attachments/assets/395cbfd0-81fd-4bd4-8eff-8f54814368d7)

-  Fungsi main(): Alur Utama Program
Fungsi ini mengatur interaksi utama dengan pengguna. Berikut urutannya:

- Register atau Login: Pengguna bisa memilih untuk mendaftar akun baru atau login.
![image](https://github.com/user-attachments/assets/f10e9d59-7f96-442b-8567-2f8f17c295a5)

- Register:

Jika memilih opsi register (1), pengguna diminta memasukkan username dan password, kemudian akun baru disimpan ke list pengguna sebagai user.
![image](https://github.com/user-attachments/assets/1875fdd3-7c1e-413d-92d6-9883c202b262)

- Login:

Jika memilih opsi login (2), program meminta username dan password.
Jika login berhasil sebagai admin, pengguna akan diberikan menu untuk menambah, menghapus, atau melihat kursi.
Jika login berhasil sebagai user, pengguna akan diberikan menu untuk melihat, memesan, atau mengembalikan kursi.
![image](https://github.com/user-attachments/assets/2f7794bd-1b2a-45be-b661-35fc7d7e82a9)

- Admin Menu:

Admin dapat menambah kursi (Tambah Kursi), menghapus kursi (Hapus Kursi), melihat daftar kursi (Lihat Kursi), atau keluar (Logout).
![image](https://github.com/user-attachments/assets/93781315-848c-4553-a132-208374fe7459)

- User Menu:

User dapat melihat daftar kursi (Lihat Kursi), memesan kursi (Pesan Kursi), mengembalikan kursi (Kembalikan Kursi), atau keluar (Logout).
![image](https://github.com/user-attachments/assets/def46ae6-1b26-47c9-b0c1-391154d9c1e2)


- Looping:

Program akan terus berjalan dalam loop sampai pengguna memilih untuk logout.


- Program Utama
Di akhir program, fungsi main() dipanggil agar program berjalan.

![image](https://github.com/user-attachments/assets/118aa37c-1b90-48ac-8aec-2d5503e985cd)

# Penjelasan Output

- Saat Program Dimulai
Ketika program dijalankan, pengguna akan melihat pesan pembuka:

![Screenshot 2024-10-14 194518](https://github.com/user-attachments/assets/10c9dcc5-02d8-46bc-af3e-b8de7447716a)

Pengguna diminta memilih untuk *register* (mendaftarkan akun user baru) atau *login* sebagai admin/user.

- Register User
Jika pengguna memilih opsi 1 (Register), outputnya akan meminta pengguna memasukkan username dan password :
![Screenshot 2024-10-14 194640](https://github.com/user-attachments/assets/30438541-3fc7-44ee-9145-9359c9bdb3f8)

Setelah mengisi data, akun baru berhasil dibuat sebagai user dan pesan konfirmasi ditampilkan.

- Login sebagai Admin
Jika pengguna memilih opsi 2 (Login) dan memasukkan username dan password admin (fauzia admin/fauzia123), maka setelah login, akan muncul menu khusus admin:

![Screenshot 2024-10-14 194824](https://github.com/user-attachments/assets/6be312de-9988-48e1-b74c-6dad4ad9e421)

Setelah login sebagai admin, pilihan yang tersedia adalah:
- Tambah kursi : Admin dapat menambahkan kursi baru ke daftar kursi.
- Hapus kursi : Admin dapat menghapus kursi dari daftar.
- Lihat kursi : Admin dapat melihat daftar kursi yang tersedia dalam bentuk tabel.
- Logout: Kembali ke menu login.

- Login sebagai User
Jika user login dengan username dan password yang sudah didaftarkan, outputnya adalah menu user:

![Screenshot 2024-10-14 213230](https://github.com/user-attachments/assets/b1593834-eab7-4082-9e94-11f40f6bf07c)

- Setelah login, user dapat memilih:
- Lihat Kursi : Menampilkan kursi yang tersedia.
- Pesan Kursi : Memesan kursi dengan jumlah dan lama waktu sewa.
- Kembalikan Kursi : Mengembalikan kursi yang sudah disewa.
- Logout : Kembali ke menu login.

- Menambahkan Kursi (Admin)
Jika admin memilih opsi "1" (Tambah Kursi), admin akan diminta memasukkan data kursi:

![Screenshot 2024-10-14 213037](https://github.com/user-attachments/assets/47d932e1-9ead-41e9-848f-8a1a17f6b4f6)

- Melihat Kursi
Jika user atau admin memilih untuk melihat kursi, program akan menampilkan daftar kursi yang tersedia dalam bentuk tabel:

![Screenshot 2024-10-14 213241](https://github.com/user-attachments/assets/4f90435c-0c43-4bd0-a10b-a93e2c4aca1f)

- Memesan Kursi (User)
Jika user memilih opsi untuk memesan kursi, output akan meminta informasi kursi yang akan disewa:

![Screenshot 2024-10-14 213253](https://github.com/user-attachments/assets/b1d25030-5576-4510-9169-207a606bf056)

Jika jumlah kursi yang dipesan melebihi stok yang tersedia, output akan menampilkan pesan kesalahan:

![Screenshot 2024-10-14 215243](https://github.com/user-attachments/assets/76e4e307-16c5-4458-8639-344ec52f723a)

- Mengembalikan Kursi (User) 
Jika user memilih opsi untuk mengembalikan kursi, output akan meminta detail pengembalian:

![Screenshot 2024-10-14 213302](https://github.com/user-attachments/assets/fbb5cef6-b4e2-4b57-a989-ff0e97294c0c)

Jika user mencoba mengembalikan lebih dari jumlah yang dipesan, maka output akan memberikan pesan kesalahan:

![Screenshot 2024-10-14 215944](https://github.com/user-attachments/assets/44b20d98-67d2-4d28-957c-366614c0de66)

- Logout
Setelah user atau admin memilih untuk logout, mereka akan kembali ke menu utama program:

![Screenshot 2024-10-14 213319](https://github.com/user-attachments/assets/c50c1031-dce0-4eba-b9a6-36870d3ee9e8)



















