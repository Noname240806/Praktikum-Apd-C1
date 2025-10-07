# Validasi Login
nama1 = "Akbar Pratama"
nim1 = "2509106091"
Percobaan = 0

while Percobaan < 3:
    print("== Login ==")
    Username = input("Masukkan Username: ")
    Password = input("Masukkan Password: ")
    
    if Username == nama1 and Password == nim1:
        print("Login Berhasil ")
        break
    else:
        Percobaan += 1
        sisa = 3 - Percobaan
        print("Login Gagal. Sisa percobaan:", sisa)

if Percobaan == 3:
    print("Program Selesai")

else:
    while True:
        print("\n== Menu Ticket ==")
        print("1. Tiket Reguler : Rp 50.000")
        print("2. Tiket VIP     : Rp 100.000") 
        print("3. Tiket VVIP    : Rp 150.000")
        print("4. Keluar")
        Pilihan = input("Pilihan Ticket [1-4]: ")

        if Pilihan == "4":
            print("Terima kasih, program selesai.")
            break

        if Pilihan == "1":
            Ticket = "Reguler"
            Harga = 50000
        elif Pilihan == "2":
            Ticket = "VIP"
            Harga = 100000
        elif Pilihan == "3":
            Ticket = "VVIP"
            Harga = 150000
        else:
            print("Pilihan tidak ada! Silakan pilih 1-4.")
            continue 

        JumlahTicket = input("Masukkan Jumlah Tiket: ")
        if not JumlahTicket.isdigit():
            print("Masukkan Angka Saja")
            continue
        jumlah = int(JumlahTicket)
        total = 0

        for A in range(jumlah):
            total += Harga

        if total >= 300000:
            potongan = total * 0.12
            totalAkhir = total - potongan
            diskon = "Diskon sebesar 12%"
        elif total >= 200000:
            potongan = total * 0.08
            totalAkhir = total - potongan
            diskon = "Diskon sebesar 8%"
        elif total >= 150000:
            potongan = 0
            totalAkhir = total
            diskon = "Poster Film Ekslusif"
        else:
            potongan = 0
            totalAkhir = total
            diskon = "Tidak dapat apa-apa"

        print("== Hasil Pembelian ==")
        print("Pilihan Ticket :", Ticket)
        print("Jumlah Ticket  :", jumlah)
        print("Total Bayar    : Rp", total)
        print("Total Akhir    : Rp", int(totalAkhir))
        print("Mendapatkan    :", diskon)