# Input data
nama = input("Masukkan Nama Lengkap: ")
nim = input("Masukkan NIM: ")
harga = int(input("Masukkan Harga Laptop: "))

# Hitung diskon dan harga akhir
diskonAcer = harga * 0.05
akhirAcer = harga - diskonAcer

diskonAsus = harga * 0.07
akhirAsus = harga - diskonAsus

diskonLenovo = harga * 0.10
akhirLenovo = harga - diskonLenovo

# Output hasil
print(f"{nama} dengan NIM {nim} ingin membeli laptop seharga Rp {harga}")
print(f"Jika membeli Laptop Acer, harga setelah diskon 5%: Rp {akhirAcer}")
print(f"Jika membeli Laptop Asus, harga setelah diskon 7%: Rp {akhirAsus}")
print(f"Jika membeli Laptop Lenovo, harga setelah diskon 10%: Rp {akhirLenovo}")