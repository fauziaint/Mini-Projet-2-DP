print("-----------Hi! Daily Camping Chairs Here-----------")
print("---------Silakan pilih menu di bawah yah!!-----------")

from prettytable import PrettyTable


pengguna = [{'username': 'fauzia admin', 'password': 'fauzia123', 'role': 'admin'}]  

kursi = []
transaksi = []

def lihat_kursi():
    if not kursi:
        print("Tidak ada kursi yang tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Kursi", "Jumlah", "Harga Sewa per Hari"]
        for idx, k in enumerate(kursi, 1):
            table.add_row([idx, k['nama'], k['jumlah'], k['harga']])
        print(table)

def tambah_kursi(nama, jumlah, harga):
    kursi.append({'nama': nama, 'jumlah': jumlah, 'harga': harga})
    print(f"Kursi {nama} berhasil ditambahkan.")

def hapus_kursi(nama):
    for k in kursi:
        if k['nama'] == nama:
            kursi.remove(k)
            print(f"Kursi {nama} berhasil dihapus.")
            return
    print(f"Kursi {nama} tidak ditemukan.")

def pesan_kursi(nama, jumlah, jumlah_hari):
    for k in kursi:
        if k['nama'] == nama:
            if k['jumlah'] >= jumlah:
                total_harga = k['harga'] * jumlah * jumlah_hari
                k['jumlah'] -= jumlah
                transaksi.append({'nama': k['nama'], 'jumlah': jumlah, 'hari': jumlah_hari, 'total': total_harga})
                print(f"Kursi {nama} berhasil dipesan sebanyak {jumlah} kursi selama {jumlah_hari} hari. Total harga: {total_harga}")
            else:
                print(f"Kursi yang tersedia hanya {k['jumlah']}, tidak cukup untuk pesanan Anda.")
            return
    print(f"Kursi {nama} tidak tersedia.")

def kembalikan_kursi(nama, jumlah):
    for trans in transaksi:
        if trans['nama'] == nama and trans['jumlah'] >= jumlah:
            trans['jumlah'] -= jumlah
            for k in kursi:
                if k['nama'] == nama:
                    k['jumlah'] += jumlah
                    print(f"Kursi {nama} berhasil dikembalikan sebanyak {jumlah}.")
                    return
    print(f"Gagal mengembalikan kursi {nama}. Pastikan jumlah yang dikembalikan valid.")

def register(username, password):
    return {'username': username, 'password': password, 'role': 'user'}

def login(username, password):
    for user in pengguna:
        if user['username'] == username and user['password'] == password:
            return user['role']
    return None

def main():
    while True:
        print("\n Penyewaan Kursi Lipat")
        print("1. Register (Hanya untuk user)")
        print("2. Login")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == '1':
            print("\n----- Register User -----")
            username = input("Username: ")
            password = input("Password: ")
            pengguna.append(register(username, password))
            print("Registrasi berhasil. Anda terdaftar sebagai user.")

        elif pilihan == '2':
            print("\n----- Login -----")
            username = input("Username: ")
            password = input("Password: ")
            role = login(username, password)
            
            if role == 'admin':
                while True:
                    print("\n------ Admin -----")
                    print("1. Tambah Kursi")
                    print("2. Hapus Kursi")
                    print("3. Lihat Kursi")
                    print("4. Logout")
                    admin_pilihan = input("Pilih opsi (1/2/3/4): ")
                    if admin_pilihan == '1':
                        nama = input("Nama kursi: ")
                        jumlah = int(input("Jumlah kursi: "))
                        harga = float(input("Harga sewa per hari: "))
                        tambah_kursi(nama, jumlah, harga)
                    elif admin_pilihan == '2':
                        nama = input("Nama kursi yang ingin dihapus: ")
                        hapus_kursi(nama)
                    elif admin_pilihan == '3':
                        lihat_kursi()
                    elif admin_pilihan == '4':
                        break
                    else:
                        print("Pilihan tidak valid.")

            elif role == 'user':
                while True:
                    print("\n----- User -----")
                    print("1. Lihat Kursi")
                    print("2. Pesan Kursi")
                    print("3. Kembalikan Kursi")
                    print("4. Logout")
                    user_pilihan = input("Pilih opsi (1/2/3/4): ")
                    if user_pilihan == '1':
                        lihat_kursi()
                    elif user_pilihan == '2':
                        nama = input("Nama kursi yang ingin dipesan: ")
                        jumlah = int(input("Jumlah kursi: "))
                        jumlah_hari = int(input("Jumlah hari sewa: "))
                        pesan_kursi(nama, jumlah, jumlah_hari)
                    elif user_pilihan == '3':
                        nama = input("Nama kursi yang ingin dikembalikan: ")
                        jumlah = int(input("Jumlah kursi yang ingin dikembalikan: "))
                        kembalikan_kursi(nama, jumlah)
                    elif user_pilihan == '4':
                        break
                    else:
                        print("Pilihan tidak valid.")
            else:
                print("Username atau password salah.")
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()