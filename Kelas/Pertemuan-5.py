# #mendefinisikan list
# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25], 
#             ['siswa', 17, False, 0,['orsikom', 25]]]
# praktikum.append('siswa2','angkatan', 24)
# print(praktikum)

# list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # Tambahkan Web
# studyclub.insert(2,"Web")
# print(studyclub)
#  output
# ['Data Science', 'Robotics', 'Web', 'Multimedia', 'Network']

# list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)
# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# studyclub[2] =["Jarkom","AI"]
# print(studyclub)

# # list awal
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# del matakuliah[2] mengapus permanen tanpa menampilkan di histori
# print(matakuliah)

# # list awal
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen dengan nilai "Kalkulus"
# matakuliah.remove('Kalkulus')
# print(matakuliah)

# # list awal
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# # print(matakuliah)
# # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# ambil_matkul = matakuliah.pop(0) # masuk ke histori
# print(matakuliah)
# print(ambil_matkul)

# # list
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# print(matakuliah[1:6:2])# 1 = ambil indek, 6 = berhenti di data sebelum 6 , 2 = itu jarak lompatan

# # Membuat Nested List
# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"]
# ["Pernanda", "Riyadi", "Ahnaf"],
# ]
# print(kelas[1][1])

# # list mahasiswa
# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     for j in i :
#         print (j)
# # i dan j merupakan variabel sementara / temporary, kita dapat menggantinya dengan apa saja asal sesuai dengan syarat nama variabel

keranjang = ["Brokoli", "Apel", "Jamur", "Nanas", "Wortel", "Kiwi", "Kol", "Sawi","Lobak"]
print(keranjang[1:5:2])
