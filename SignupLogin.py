# membuat sistem sign up dan login di python
# import package
import sys
import time
import os


asd2 = "Ini adalah contoh sistem login sederhana yang belum sepenuhnya maksimal"
asd1 = "Pastikan anda memilih signup dulu sebelum login karena data user tidak disimpan"

# clear terminal dsb
os.system("cls")
print(asd2.center(20), asd1.center(20))
print("")
time.sleep(1.2)
# menu sign up  or log in
# pengulangan
x = "curut"
while x == "curut":
    # signup lalu login
    print("signup")
    print("login")
    pilih1 = input("masukkan pilihan =>>")
    # pilih signup :
    if pilih1 == "signup":
        time.sleep(1)
        user = input("masukkan username =>>")
        password = input("masukkan password =>>")
        time.sleep(0.5)
        print(f"username anda {user} & password anda {password}")
        print("pastikan anda tetap ingat username & password anda")
        time.sleep(1)
    # lalu login :
    elif pilih1 == "login":
        time.sleep(1)
        name = input("masukkan username anda =>>")
        pw = input("masukkan password anda =>>")
        if name == user and pw == password:
            # jika username & password berhasil
            print("selamat datang, Anda berhasil login")
            time.sleep(2.3)
        else:
            # jika username & password tidak berhasil
            print("gagal")
            sys.exit()
