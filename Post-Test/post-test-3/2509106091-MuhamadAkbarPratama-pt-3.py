#Validasi Login
nama1 = "Akbar Pratama"
nim1 = "2509106091"
biayaLangganan = 1500000

print("Masukkan Nama")
nama = input()
print("Masukkan NIM")
nim = input()

#Opsi Pembayaran Biaya Langganan Aplikasi Streaming Musik:
if nama == nama1 and nim == nim1:
    print("Login Berhasil\n")
    print("=== Pilih Paket Langganan ===")
    print("1. Bronze   : Biaya administrasi (1%)")
    print("2. Silver   : Biaya administrasi (3%)")
    print("3. Gold     : Biaya administrasi (5%)")
    print("4. Platinum : Biaya administrasi (7%)")

    pilihan = input("Pilih paket [1-4]: ")

    if pilihan == "1":
        namaPaket = "Bronze"
        biayaAdmin = 0.01
        fitur = "akses dasar ke lagu-lagu populer"
    elif pilihan == "2":
        namaPaket = "Silver"
        biayaAdmin = 0.03
        fitur = "akses lagu premium dan playlist kustom"
    elif pilihan == "3":
        namaPaket = "Gold"
        biayaAdmin = 0.05
        fitur = "akses lagu premium, playlist kustom, dan mode offline"
    elif pilihan == "4":
        namaPaket = "Platinum"
        biayaAdmin = 0.07
        fitur = "akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"
    else:
        print("Pilihan paket tidak valid!")
        exit()
    #Rumus
    totalBayar = biayaLangganan + biayaLangganan * biayaAdmin

    # Tampilan Hasil
    print("\n=== Detail Langganan ===")
    print("Nama        :", nama)
    print("NIM         :", nim)
    print("Paket       :", namaPaket)
    print("Fitur       :", fitur)
    print("Total Bayar : Rp " + str(int(totalBayar)))
else:
    print("Login Gagal! Nama & NIM Salah")