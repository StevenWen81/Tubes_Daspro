'''
MODUL F99 Analytics
v. 30 April 2021
Spesifikasi: Kumpulan berbagai fungsi yang bermanfaat
'''

# KAMUS LOKAL
# Deklarasi variabel
# type arr_full of <type> :
#   (
#       arr_csv : arr of arr of of <type>,
#       n_eff : int,
#       n_col : int
# )

# Deklarasi fungsi dan prosedur
def charAreInt(text):
    # Spesifikasi : Mengecek apakan inputan : str bisa dijadikan int
    # KAMUS LOKAL LOKAL
    # text : str
    # char : char
    # areInt : bool
    # ALGORITMA
    areInt = True
    for char in text:
        if not (48 <= ord(char) <= 57):
            areInt = False
    return areInt


def isTahun(tahun):
    # Spesifikasi : Mengecek apakah tahun int berformat YYYY
    # ALGORITMA
    if charAreInt(tahun):
        if 1000 <= int(tahun) <= 9999:
            return True
        else:
            return False
    else:
        return False


def isAdmin(logged_user, user_data):
    # Spesifikasi : Mengecek apakah pengguna adalah admin
    # KAMUS LOKAL LOKAL
    # arr_full : arr_full
    # lines : arr of str
    # f, logged_user : str
    # idx : int
    # userIsAdmin : bool
    # ALGORITMA
    userIsAdmin = False
    idx = 0
    for i in range(1, (len(user_data) - 1)):  # Pengecekan username
        if logged_user == user_data[i][1]:  # Asumsi logged user ada di user.csv
            idx = i

    if user_data[idx][5].lower() == "admin":
        userIsAdmin = True
        
    return userIsAdmin
