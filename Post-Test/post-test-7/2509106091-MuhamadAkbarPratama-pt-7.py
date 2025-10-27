# PROGRAM MISI LUAR ANGKASA 

pengguna = [
    ("Akbar", "123", "admin") 
]

misi_luar_angkasa = [
    {"nama": "Voyager 1", "tahun": 1977, "negara": "Amerika Serikat", "jenis": "Probe", "tujuan": "Eksplorasi ruang antar bintang"},
    {"nama": "Apollo 11", "tahun": 1969, "negara": "Amerika Serikat", "jenis": "Misi Berawak", "tujuan": "Pendaratan di Bulan"},
    {"nama": "Tianwen-1", "tahun": 2020, "negara": "China", "jenis": "Rover", "tujuan": "Eksplorasi Mars"},
    {"nama": "Rosetta", "tahun": 2004, "negara": "Eropa", "jenis": "Probe", "tujuan": "Meneliti Komet 67P"},
    {"nama": "James Webb", "tahun": 2021, "negara": "Internasional", "jenis": "Teleskop", "tujuan": "Mengamati galaksi dan bintang jauh"}
]

login_user = None


def hitung_jumlah_misi():
    return len(misi_luar_angkasa)

def cari_misi_berdasarkan_tahun(tahun):
    hasil = [m for m in misi_luar_angkasa if m["tahun"] == tahun]
    return hasil

def tampilkan_pengguna_terdaftar():
    if not pengguna:
        return "Belum ada pengguna yang terdaftar."
    else:
        daftar = [f"Nama: {p[0]} | Role: {p[2]}" for p in pengguna]
        return "\n".join(daftar)

def validasi_login(nama, katasandi):
    global login_user
    login_user = next((p for p in pengguna if p[0] == nama and p[1] == katasandi), None)
    return login_user

def tampilkan_semua_misi():
    if not misi_luar_angkasa:
        print("Belum ada data misi.")
    else:
        print("\n=== DAFTAR MISI LUAR ANGKASA ===")
        for i, m in enumerate(misi_luar_angkasa, start=1):
            print(f"{i}. Nama: {m['nama']} | Tahun: {m['tahun']} | Negara: {m['negara']} | Jenis: {m['jenis']} | Tujuan: {m['tujuan']}")
        print()

def tambah_misi():
    global misi_luar_angkasa
    try:
        nama_misi = input("Nama Misi: ")
        tahun = int(input("Tahun: "))
        negara = input("Negara: ")
        jenis = input("Jenis Misi: ")
        tujuan = input("Tujuan Misi: ")
        misi_luar_angkasa.append({
            "nama": nama_misi,
            "tahun": tahun,
            "negara": negara,
            "jenis": jenis,
            "tujuan": tujuan
        })
        print("Misi baru berhasil ditambahkan!")
    except ValueError:
        print("Error. Tahun harus berupa angka!")

def ubah_misi():
    tampilkan_semua_misi()
    try:
        idx = int(input("Masukkan nomor misi yang ingin diubah: ")) - 1
        if 0 <= idx < len(misi_luar_angkasa):
            m = misi_luar_angkasa[idx]
            print(f"Data lama: {m}")
            m["nama"] = input(f"Nama baru ({m['nama']}): ") or m["nama"]
            m["tahun"] = int(input(f"Tahun baru ({m['tahun']}): ") or m["tahun"])
            m["negara"] = input(f"Negara baru ({m['negara']}): ") or m["negara"]
            m["jenis"] = input(f"Jenis baru ({m['jenis']}): ") or m["jenis"]
            m["tujuan"] = input(f"Tujuan baru ({m['tujuan']}): ") or m["tujuan"]
            print("Data misi berhasil diperbarui!")
        else:
            print("Nomor misi tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_misi():
    11
    tampilkan_semua_misi()
    try:
        idx = int(input("Masukkan nomor misi yang ingin dihapus: ")) - 1
        if 0 <= idx < len(misi_luar_angkasa):
            del misi_luar_angkasa[idx]
            print("Data misi berhasil dihapus!")
        else:
            print("Nomor misi tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

while True:
    print("""
=========================================
|           MENU PEMDAFTARAN            |
=========================================
| 1. Registrasi                         |
| 2. Login                              |
| 3. Lihat Pengguna                     |
| 4. Keluar                             |
=========================================
""")
    menu = input("Pilih menu (1-4): ")

    if menu == "1":
        print("=== REGISTRASI PENGGUNA BARU ===")
        nama = input("Masukkan nama pengguna: ")
        katasandi = input("Masukkan kata sandi: ")
        role = input("Masukkan role (admin/pengguna): ")

        if any(p[0] == nama for p in pengguna):
            print("Nama pengguna sudah terdaftar!")
        elif role not in ("admin", "pengguna"):
            print("Role tidak valid.")
        else:
            pengguna.append((nama, katasandi, role))
            print("Registrasi berhasil!")

    elif menu == "2":
        nama = input("Masukkan nama pengguna: ")
        katasandi = input("Masukkan kata sandi: ")

        if validasi_login(nama, katasandi):
            print(f"Selamat datang, {login_user[0]}! Role: {login_user[2]}")

            if login_user[2] == "admin":
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
                        print(f"Total misi: {hitung_jumlah_misi()}")
                    elif pilih == "2":
                        tambah_misi()
                    elif pilih == "3":
                        ubah_misi()
                    elif pilih == "4":
                        hapus_misi()
                    elif pilih == "5":
                        try:
                            tahun = int(input("Masukkan tahun misi: "))
                            hasil = cari_misi_berdasarkan_tahun(tahun)
                            if hasil:
                                print("\nHasil pencarian:")
                                for m in hasil:
                                    print(f"Nama: {m['nama']} | Negara: {m['negara']}")
                            else:
                                print("Tidak ada misi pada tahun tersebut.")
                        except ValueError:
                            print("Error: Tahun harus angka!")
                    elif pilih == "6":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid!")

            else:
                while True:
                    print("""
=========================
|     MENU PENGGUNA     |
=========================
| 1. Lihat Data Misi     |
| 2. Logout              |
=========================
""")
                    pilih = input("Pilih menu (1-2): ")

                    if pilih == "1":
                        tampilkan_semua_misi()
                    elif pilih == "2":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid!")
        else:
            print("Login gagal, periksa nama atau sandi.")

    elif menu == "3":
        print("=== PENGGUNA TERDAFTAR ===")
        print(tampilkan_pengguna_terdaftar())

    elif menu == "4":
        print("Keluar")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
