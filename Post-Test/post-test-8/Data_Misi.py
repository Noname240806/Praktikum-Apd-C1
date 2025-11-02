from prettytable import PrettyTable

misi_luar_angkasa = [
    {"nama": "Voyager 1", "tahun": 1977, "negara": "Amerika Serikat", "jenis": "Probe", "tujuan": "Eksplorasi ruang antar bintang"},
    {"nama": "Apollo 11", "tahun": 1969, "negara": "Amerika Serikat", "jenis": "Misi Berawak", "tujuan": "Pendaratan di Bulan"},
    {"nama": "Tianwen-1", "tahun": 2020, "negara": "China", "jenis": "Rover", "tujuan": "Eksplorasi Mars"},
    {"nama": "Rosetta", "tahun": 2004, "negara": "Eropa", "jenis": "Probe", "tujuan": "Meneliti Komet 67P"},
    {"nama": "James Webb", "tahun": 2021, "negara": "Internasional", "jenis": "Teleskop", "tujuan": "Mengamati galaksi dan bintang jauh"}
]

def hitung_jumlah_misi():
    return len(misi_luar_angkasa)

def cari_misi_berdasarkan_tahun(tahun):
    return [m for m in misi_luar_angkasa if m["tahun"] == tahun]

def tampilkan_semua_misi():
    if not misi_luar_angkasa:
        print("Belum ada data misi.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama", "Tahun", "Negara", "Jenis", "Tujuan"]

    for i, m in enumerate(misi_luar_angkasa, start=1):
        table.add_row([i, m["nama"], m["tahun"], m["negara"], m["jenis"], m["tujuan"]])

    print(table)
    print(f"Total misi: {hitung_jumlah_misi()}")

def tambah_misi():
    try:
        nama = input("Nama Misi: ")
        tahun = int(input("Tahun: "))
        negara = input("Negara: ")
        jenis = input("Jenis: ")
        tujuan = input("Tujuan: ")

        misi_luar_angkasa.append({
            "nama": nama,
            "tahun": tahun,
            "negara": negara,
            "jenis": jenis,
            "tujuan": tujuan
        })
        print("Misi berhasil ditambahkan!")
    except ValueError:
        print("Tahun harus berupa angka!")

def ubah_misi():
    tampilkan_semua_misi()
    try:
        idx = int(input("Masukkan nomor misi yang ingin diubah: ")) - 1
        if 0 <= idx < len(misi_luar_angkasa):
            m = misi_luar_angkasa[idx]
            m["nama"] = input(f"Nama baru ({m['nama']}): ") or m["nama"]
            m["tahun"] = int(input(f"Tahun baru ({m['tahun']}): ") or m["tahun"])
            m["negara"] = input(f"Negara baru ({m['negara']}): ") or m["negara"]
            m["jenis"] = input(f"Jenis baru ({m['jenis']}): ") or m["jenis"]
            m["tujuan"] = input(f"Tujuan baru ({m['tujuan']}): ") or m["tujuan"]
            print("Data berhasil diperbarui!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_misi():
    tampilkan_semua_misi()
    try:
        idx = int(input("Masukkan nomor misi yang ingin dihapus: ")) - 1
        if 0 <= idx < len(misi_luar_angkasa):
            del misi_luar_angkasa[idx]
            print("Misi berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")
