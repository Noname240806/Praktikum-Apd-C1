from Login_Misi import registrasi, login, tampilkan_pengguna, login_user
from Data_Misi import tampilkan_semua_misi, tambah_misi, ubah_misi, hapus_misi, cari_misi_berdasarkan_tahun

while True:
    print("""
=========================================
|           MENU UTAMA                 |
=========================================
| 1. Registrasi                        |
| 2. Login                             |
| 3. Lihat Pengguna                    |
| 4. Keluar                            |
=========================================
""")
    menu = input("Pilih menu (1-4): ")

    if menu == "1":
        registrasi()

    elif menu == "2":
        user = login()
        if user:
            if user[2] == "admin":
                while True:
                    print("""
=========================
|      MENU ADMIN        |
=========================
| 1. Lihat Semua Misi    |
| 2. Tambah Misi Baru    |
| 3. Ubah Data Misi      |
| 4. Hapus Data Misi     |
| 5. Cari Misi (Tahun)   |
| 6. Logout              |
=========================
""")
                    pilih = input("Pilih menu (1-6): ")

                    if pilih == "1":
                        tampilkan_semua_misi()
                    elif pilih == "2":
                        tambah_misi()
                    elif pilih == "3":
                        ubah_misi()
                    elif pilih == "4":
                        hapus_misi()
                    elif pilih == "5":
                        try:
                            tahun = int(input("Masukkan tahun: "))
                            hasil = cari_misi_berdasarkan_tahun(tahun)
                            if hasil:
                                from prettytable import PrettyTable
                                table = PrettyTable()
                                table.field_names = ["Nama", "Negara", "Tahun"]
                                for m in hasil:
                                    table.add_row([m["nama"], m["negara"], m["tahun"]])
                                print(table)
                            else:
                                print("Tidak ada misi pada tahun tersebut.")
                        except ValueError:
                            print("Tahun harus angka!")
                    elif pilih == "6":
                        break
                    else:
                        print("Pilihan tidak valid!")

            else:
                while True:
                    print("""
=========================
|     MENU PENGGUNA     |
=========================
| 1. Lihat Data Misi    |
| 2. Logout             |
=========================
""")
                    pilih = input("Pilih menu (1-2): ")

                    if pilih == "1":
                        tampilkan_semua_misi()
                    elif pilih == "2":
                        break
                    else:
                        print("Pilihan tidak valid!")

    elif menu == "3":
        tampilkan_pengguna()

    elif menu == "4":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid!")
