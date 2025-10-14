# PROGRAM MISI LUAR ANGKASA

pengguna = []
misi_luar_angkasa = [
    ["Voyager 1", 1977, "Amerika Serikat", "Probe", "Eksplorasi ruang antar bintang"],
    ["Apollo 11", 1969, "Amerika Serikat", "Misi Berawak", "Pendaratan di Bulan"],
    ["Tianwen-1", 2020, "China", "Rover", "Eksplorasi Mars"],
    ["Rosetta", 2004, "Eropa", "Probe", "Meneliti Komet 67P"],
    ["James Webb", 2021, "Internasional", "Teleskop", "Mengamati galaksi dan bintang jauh"]
]
login_user = None

while True:
    print("""
=========================================
|            MENU PEMDAFTARAN           |
=========================================
| 1. Registrasi                         |
| 2. Login                              |
| 3. Keluar                             |
=========================================
""")
    menu = input("Pilih menu(1-3):")

    if menu == "1":
        print("=== Registrasi Pengguna Baru ===")
        nama = input("Masukkan nama pengguna: ")
        katasandi = input("Masukkan kata sandi: ")

        while True:
            role = input("Masukkan role (admin/pengguna): ")
            if role in ("admin", "pengguna"):
                break
            else:
                print("Role tidak valid, hanya boleh admin/pengguna.")

        sudah_ada = False
        for p in pengguna:
            if p[0] == nama:
                sudah_ada = True
                break

        if sudah_ada:
            print("Nama pengguna sudah terdaftar!")
        else:
            pengguna.append((nama, katasandi, role))
            print("Registrasi berhasil!")

    elif menu == "2":
        if not pengguna:
            print("Belum ada pengguna yang terdaftar.")
        else:
            nama = input("Masukkan nama pengguna: ")
            katasandi = input("Masukkan kata sandi: ")

            login_user = None
            for p in pengguna:
                if p[0] == nama and p[1] == katasandi:
                    login_user = p
                    break

            if login_user is None:
                print("Login gagal, periksa kembali nama dan sandi.")
            else:
                print(f"Selamat datang, {login_user[0]}!")

                if login_user[2] == "admin":
                    while True:
                        print("""
=========================
|      MENU ADMIN        |
=========================
| 1. Lihat Semua Misi    |
| 2. Tambah Misi Baru     |
| 3. Ubah Data Misi       |
| 4. Hapus Data Misi      |
| 5. Keluar               |
=========================
""")
                        pilih = input("Pilih menu(1-5): ")

                        if pilih == "1":
                            if not misi_luar_angkasa:
                                print("Belum ada data misi.")
                            else:
                                print("=== DATA MISI LUAR ANGKASA ===")
                                for i, m in enumerate(misi_luar_angkasa):
                                    print(f"{i}. Nama: {m[0]}, Tahun: {m[1]}, Negara: {m[2]}, Jenis: {m[3]}, Tujuan: {m[4]}")

                        elif pilih == "2":
                            print("=== Tambah Data Misi ===")
                            nama_misi = input("Nama Misi: ")
                            tahun = input("Tahun: ")
                            negara = input("Negara: ")
                            jenis = input("Jenis Misi: ")
                            tujuan = input("Tujuan Misi: ")
                            misi_luar_angkasa.append([nama_misi, tahun, negara, jenis, tujuan])
                            print("Data misi berhasil ditambahkan!")

                        elif pilih == "3":
                            print("=== Ubah Data Misi ===")
                            lihat = input("Masukkan nomor misi yang ingin diubah: ")
                            if lihat.isdigit() and 1 <= int(lihat) <= len(misi_luar_angkasa):
                                idx = int(lihat) - 1
                                print(f"Data lama: {misi_luar_angkasa[idx]}")
                                nama_baru = input("Nama baru: ")
                                tahun_baru = input("Tahun baru: ")
                                negara_baru = input("Negara baru: ")
                                jenis_baru = input("Jenis baru: ")
                                tujuan_baru = input("Tujuan baru: ")
                                misi_luar_angkasa[idx] = [nama_baru, tahun_baru, negara_baru, jenis_baru, tujuan_baru]
                                print("Data berhasil diubah!")
                            else:
                                print("Nomor tidak valid.")

                        elif pilih == "4":
                            print("=== Hapus Data Misi ===")
                            hapus = input("Masukkan nomor misi yang ingin dihapus: ")
                            if hapus.isdigit() and 1 <= int(hapus) <= len(misi_luar_angkasa):
                                del misi_luar_angkasa[int(hapus) - 1]
                                print("Data misi berhasil dihapus!")
                            else:
                                print("Nomor tidak valid.")

                        elif pilih == "5":
                            login_user = None
                            break
                        else:
                            print("Pilihan tidak valid.")

                else:
                    while True:
                        print("""
=========================
|    MENU PENGGUNA       |
=========================
| 1. Lihat Data Misi     |
| 2. Keluar              |
=========================
""")
                        pilih = input("Pilih menu: ")

                        if pilih == "1":
                            print("\n=== DAFTAR MISI LUAR ANGKASA ===")
                            for i, m in enumerate(misi_luar_angkasa, start=1):
                                print(f"{i}. Nama: {m[0]}, Tahun: {m[1]}, Negara: {m[2]}, Jenis: {m[3]}, Tujuan: {m[4]}")
                        elif pilih == "2":
                            login_user = None
                            break
                        else:
                            print("Pilihan tidak valid.")

    elif menu == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")