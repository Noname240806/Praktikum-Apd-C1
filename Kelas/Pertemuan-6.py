# Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# for i in buah: 
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9} 

# for angka in angka_ganjil:     
#     print(angka) 

# angka_ganjil.remove(11)
# print(angka_ganjil)

# Daftar_buku = { 
#  	"Buku1" : "Bumi Manusia", #“key/kunci : value/nilai”. 
#  	"Buku2" : "Laut Bercerita",
#     "Buku3" : "Bumi Bercerita Manusia"
# } 
# print(Daftar_buku["Buku1"])
# print(Daftar_buku)
# for i in Daftar_buku.values():
#     print(i)
# key/kunci itu sebelah kiri, 
# Value/nilai itu sebelah kanan, 
# item itu semua isi daftar buku

# Biodata = { 
#       "Nama" : "Ananda Daffa Harahap", 
#       "NIM" : 2409106050, 
#       "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"], 
#       "Mahasiswa_Aktif" : True, 
# }
# for i in Biodata.values():
#     print(i)

# Film = { 
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror" 
# } 
# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 
# #Sebelum Dihapus print(data) 
# del data["Nama"]
# #Setelah diubah 
# print(data) 
# #memanggil data yang telah dihapus print(data.get("Nama")) 
# {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
# {'Umur': 19, 'Jurusan': 'Informatika'} 
 
# None 
Musik = { 
"The Chainsmoker" : ["All we Know", "The Paris"], 
"Alan Walker" : ["Alone", "Lily"], 
"Neffex" : ["Best of Me", "Memories"] 
} 
 
for i, j in Musik.items(): 
 print(f"Musik milik {i} adalah : ") 
 for song in j:  
  print(song)  
  print("") 
