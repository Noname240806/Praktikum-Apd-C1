# PROGRAM MISI LUAR ANGKASA 
pengguna = []
misi_luar_angkasa = [
    {
        "nama": "Voyager 1",
        "tahun": 1977,
        "negara": "Amerika Serikat",
        "jenis": "Probe",
        "tujuan": "Eksplorasi ruang antar bintang"
    },
    {
        "nama": "Apollo 11",
        "tahun": 1969,
        "negara": "Amerika Serikat",
        "jenis": "Misi Berawak",
        "tujuan": "Pendaratan di Bulan"
    },
    {
        "nama": "Tianwen-1",
        "tahun": 2020,
        "negara": "China",
        "jenis": "Rover",
        "tujuan": "Eksplorasi Mars"
    },
    {
        "nama": "Rosetta",
        "tahun": 2004,
        "negara": "Eropa",
        "jenis": "Probe",
        "tujuan": "Meneliti Komet 67P"
    },
    {
        "nama": "James Webb",
        "tahun": 2021,
        "negara": "Internasional",
        "jenis": "Teleskop",
        "tujuan": "Mengamati galaksi dan bintang jauh"
    }
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
    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        print("=== Registrasi Pengguna Baru ===")
        nama = input("Masukkan nama pengguna: ")
        katasandi = input("Masukkan kata sandi: ")

        while True:
            role = input("Masukkan role (admin/pengguna): ").lower()
            if role in ("admin", "pengguna"):
                break
            else:
                print("Role tidak valid, hanya boleh admin/pengguna.")

        sudah_ada = any(p[0] == nama for p in pengguna)
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

            login_user = next((p for p in pengguna if p[0] == nama and p[1] == katasandi), None)

            if login_user is None:
                print("Login gagal, periksa kembali nama dan sandi.")
            else:
                print(f"Selamat datang, {login_user[0]}!")

                # === MENU ADMIN ===
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
| 5. Keluar              |
=========================
""")
                        pilih = input("Pilih menu (1-5): ")

                        if pilih == "1":
                            if not misi_luar_angkasa:
                                print("Belum ada data misi.")
                            else:
                                print("=== DATA MISI LUAR ANGKASA ===")
                                for i, m in enumerate(misi_luar_angkasa, start=1):
                                    print(f"{i}. Nama: {m['nama']}, Tahun: {m['tahun']}, Negara: {m['negara']}, Jenis: {m['jenis']}, Tujuan: {m['tujuan']}")

                        elif pilih == "2":
                            print("=== Tambah Data Misi ===")
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
                            print("Data misi berhasil ditambahkan!")

                        elif pilih == "3":
                            print("=== Ubah Data Misi ===")
                            for i, m in enumerate(misi_luar_angkasa, start=1):
                                print(f"{i}. {m['nama']} ({m['tahun']})")

                            idx = input("Masukkan nomor misi yang ingin diubah: ")
                            if idx.isdigit() and 1 <= int(idx) <= len(misi_luar_angkasa):
                                i = int(idx) - 1
                                m = misi_luar_angkasa[i]
                                print(f"Data lama: {m}")
                                m["nama"] = input(f"Nama baru ({m['nama']}): ") or m["nama"]
                                m["tahun"] = input(f"Tahun baru ({m['tahun']}): ") or m["tahun"]
                                m["negara"] = input(f"Negara baru ({m['negara']}): ") or m["negara"]
                                m["jenis"] = input(f"Jenis baru ({m['jenis']}): ") or m["jenis"]
                                m["tujuan"] = input(f"Tujuan baru ({m['tujuan']}): ") or m["tujuan"]
                                print("Data berhasil diubah!")
                            else:
                                print("Nomor tidak valid.")

                        elif pilih == "4":
                            print("=== Hapus Data Misi ===")
                            for i, m in enumerate(misi_luar_angkasa, start=1):
                                print(f"{i}. {m['nama']} ({m['tahun']})")
                            idx = input("Masukkan nomor misi yang ingin dihapus: ")
                            if idx.isdigit() and 1 <= int(idx) <= len(misi_luar_angkasa):
                                del misi_luar_angkasa[int(idx) - 1]
                                print("Data misi berhasil dihapus!")
                            else:
                                print("Nomor tidak valid.")

                        elif pilih == "5":
                            login_user = None
                            break
                        else:
                            print("Pilihan tidak valid.")

                # === MENU PENGGUNA ===
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
                                print(f"{i}. Nama: {m['nama']}, Tahun: {m['tahun']}, Negara: {m['negara']}, Jenis: {m['jenis']}, Tujuan: {m['tujuan']}")
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