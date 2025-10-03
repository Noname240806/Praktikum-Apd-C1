# ulangi = 10
# for i in range (ulangi):
#   print(f'Perulangan ke {i}')

# for i in range (1,10,3):
#   print(f'Perulangan ke {i}')

# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)

# simpan = [2, 'DUPUPU', 3.59, True]
# for i in simpan:
#     print(i)

# simpan = [3, 'ADUDU', 3.39, True]
# for i in simpan:
#     print(i)


# for i in range(1, 11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i * j}')
# print('') 

# for i in range(5):
#     for j in range(0, i+1):
#         print(f"#", end="")
# print("")

# while True:
#     print("ulang")

# jawab = 'ya'
# jawan2 = 'Tidak'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
# while(jawan2 == 'Tidak'):
#     hitung += 0
#     jawan2 = input("Selesai? ")
# print(f"Total perulangan: {hitung}")

# angka = [2, 5, 8, 12, 15, 7, 20, 28, 32]
# print("Mencari angka pertama yang lebih besar dari 10...")
# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"Angka genap ditemukan: {i}")#ga dianggap -_-
print("\nProgram selesai.")