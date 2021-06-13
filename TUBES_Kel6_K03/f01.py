'''
MODUL F01 - Register
v. 30 April 2021
Spesifikasi: Untuk admin. Mendaftarkan data user baru dengan username unik
I.S. username orang yang sedang login, lalu inputan
F.S. sebuah string yang siap di-append ke user.csv saat save
'''

import f99_analytics as f99, hashing

# KAMUS LOKAL
# Deklarasi variabel
# type userline : 
#   [
#       id : str
#       username : str
#       nama : str
#       alamat : str
#       password : str
#       role : str
# ]

# Deklarasi fungsi dan prosedur
def register(user_data, logged_user):
    # Spesifikasi : fungsi utama modul, register user baru
    # KAMUS LOKAL LOKAL
    # userline : userline
    # user_data : arr of userline
    # logged_user : str
    # isAdmin : bool
    # ALGORITMA
    userline = [
            "<0. id>", 
            "<1. username>", 
            "<2. nama>", 
            "<3. alamat>", 
            "<4. password>", 
            "user"
        ] # Inisialisasi

    if f99.isAdmin(logged_user, user_data):
        userline[2] = input("Masukkan nama: ")
        userline[1] = input("Masukkan username: ")

        while usernameNotUnique(userline[1], user_data):  # Loop pengecekan username
            print("Username sudah dipakai. Mohon masukkan username unik.")
            userline[1] = input("Masukkan username: ")

        userline[4] = hashing.encrypt(input("Masukkan password: "))
        userline[3] = input("Masukkan alamat: ")
        userline[0] = str(int(user_data[len(user_data) - 1][0]) + 1)  # last id + 1

        print("User " + userline[1] + " berhasil register sementara ke dalam Kantong Ajaib.")
        user_data.append(userline)
        return user_data

    else:  # isAdmin False
        print("Ditolak! Akses terbatas admin.")
        return "notAdmin"


def usernameNotUnique(username, user_data):
    # Spesifikasi : mengecek keunikan username
    # KAMUS LOKAL LOKAL
    # user_data : arr of arr of str
    # username : str
    # notUnique : bool
    # ALGORITMA
    notUnique = False  # Inisialisasi
    for i in range(1, (len(user_data) - 1)):
        if username == user_data[i][1]:
            notUnique = True
    return notUnique
