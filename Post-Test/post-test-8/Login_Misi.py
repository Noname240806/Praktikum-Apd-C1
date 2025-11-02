pengguna = [("Akbar", "123", "admin")]
login_user = None

def registrasi():
    global pengguna
    nama = input("Masukkan nama pengguna: ")
    sandi = input("Masukkan kata sandi: ")
    role = input("Masukkan role (admin/pengguna): ")

    if any(p[0] == nama for p in pengguna):
        print("Nama sudah terdaftar!")
    elif role not in ("admin", "pengguna"):
        print("Role tidak valid!")
    else:
        pengguna.append((nama, sandi, role))
        print("Registrasi berhasil!")

def login():
    global login_user
    nama = input("Masukkan nama pengguna: ")
    sandi = input("Masukkan kata sandi: ")
    login_user = next((p for p in pengguna if p[0] == nama and p[1] == sandi), None)

    if login_user:
        print(f"Selamat datang, {login_user[0]}! (Role: {login_user[2]})")
    else:
        print("Login gagal!")
    return login_user

def tampilkan_pengguna():
    from prettytable import PrettyTable

    if not pengguna:
        print("Belum ada pengguna.")
        return

    table = PrettyTable()
    table.field_names = ["Nama", "Role"]
    for p in pengguna:
        table.add_row([p[0], p[2]])
    print(table)
