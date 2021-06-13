'''
MODUL F05 - MENAMBAH ITEM
v. 30 April 2021
Spesifikasi : Untuk admin. Menambah ke inventory: (1) gadget, dengan 
awalan id "G", dengan atribut id, nama, deskripsi, jumlah, rarity (C, B, A, S), 
tahun; (2) consumable, dengan atribut id, nama, deskripsi, jumlah, rarity; jika 
bukan (1) atau (2) maka error.
I.S. username orang yang sedang login, lalu inputan
F.S. append data baru ke global gadget_data atau consumable_data jika ada
'''

import f99_analytics as f99

# KAMUS LOKAL
# Deklarasi variabel
# type gadget :
#   [
#       id : str
#       nama : str 
#       desc : str
#       jumlah : st
#       rarity : str
#       tahun : str
# ]
# type consumable :
#   [
#       id : str
#       nama : str 
#       desc : str
#       jumlah : st
#       rarity : str
# ]
# Deklarasi fungsi dan prosedur
def tambahitem(gadget_data, consumable_data, user_data, logged_user):
    # Spesifikasi : sebagaimana spesifikasi modul
    # KAMUS LOKAL LOKAL
    # id, id_status : str
    # gadget_data : arr of arr of str
    # ALGORITMA
    if f99.isAdmin(logged_user, user_data):
        id = input("Masukkan ID: ")
        id_status = checkId(id, gadget_data, consumable_data)

        if id_status == "idIsGadget":
            return_arr = tambahGadget(id, gadget_data)
            return(return_arr, "null")

        elif id_status == "idIsConsum":
            return_arr = tambahConsum(id, consumable_data)
            return("null", return_arr)

        elif id_status == "idAlreadyExist":
            print("Gagal menambahkan item karena ID sudah ada.")
            return ("null", "null")

        else:
            print("Gagal menambahkan item karena ID tidak valid.")
            return ("null", "null")

    else:  # logged_user is not admin
        print("Halt! Fungsi terbatas admin.")
        return ("null", "null")


def checkId(id, gadget_data, consumable_data):
    # Spesifikasi : mengecek kevalidan ID
    # KAMUS LOKAL LOKAL
    # gadget_data : arr of gadget
    # row : gadget
    # id, return_str : str
    # ALGORITMA
    return_str = "idNotValid"
    if id[0] == "G":  # untuk gadget
        return_str = "idIsGadget"

        for row in gadget_data:
            if row[0] == id:
                return_str = "idAlreadyExist"

        return return_str

    elif id[0] == "C":  # untuk consumable
        return_str = "idIsConsum"

        for row in consumable_data:
            if row[0] == id:
                return_str = "idAlreadyExist"

        return return_str
    


def tambahGadget(id, gadget_data):
    # Spesifikasi : Menginput data gadget, mengecek kevalidan, menyimpan.
    # Diasumsikan inputan bisa apapun, dengan modul berhenti jika salah input.
    # KAMUS LOKAL LOKAL
    # id : str
    # gadget : gadget
    # ALGORITMA
    gadget = [
        "<0. id>",
        "<1. nama>",
        "<2. desc>",
        "<3. jumlah>",
        "<4. rarity>",
        "<5. tahun>"
    ]
    gadget[0] = id
    gadget[1] = input("Masukkan Nama Gadget: ")
    gadget[2] = input("Masukkan Deskripsi: ")

    gadget[3] = input("Masukkan Jumlah: ")
    while not f99.charAreInt(gadget[3]):
        print("Input jumlah tidak valid!")
        gadget[3] = input("Masukkan Jumlah: ")
    # jumlah : int

    gadget[4] = input("Masukkan Rarity: ")
    while not rarityValid(gadget[4]):
        print("Input rarity tidak valid!")
        gadget[4] = input("Masukkan Rarity: ")
    # rarity is valid

    gadget[5] = input("Masukkan tahun ditemukan: ")
    while not f99.isTahun(gadget[5]):
        print("Input tahun tidak valid!")
        gadget[5] = input("Masukkan tahun ditemukan: ")
    # tahun is tahun

    print(gadget[1] + "(x" + gadget[3] + ") ditambahkan ke database sementara.")
    gadget_data.append(gadget)
    return gadget_data
    


def tambahConsum(id, consumable_data):
    # Spesifikasi : Menginput data consumable, mengecek kevalidan, menyimpan.
    # Diasumsikan inputan bisa apapun.
    # KAMUS LOKAL LOKAL
    # consumable : consumable
    # ALGORITMA
    consumable = [
        "<0. id>",
        "<1. nama>",
        "<2. desc>",
        "<3. jumlah>",
        "<4. rarity>"
    ]
    consumable[0] = id
    consumable[1] = input("Masukkan Nama Consumable: ")
    consumable[2] = input("Masukkan Deskripsi: ")

    consumable[3] = input("Masukkan Jumlah: ")
    while not f99.charAreInt(consumable[3]):
        print("Input jumlah tidak valid!")
        consumable[3] = input("Masukkan Jumlah: ")
    # jumlah : int

    consumable[4] = input("Masukkan Rarity: ")
    while not rarityValid(consumable[4]):
        print("Input rarity tidak valid!")
        consumable[4] = input("Masukkan Rarity: ")
    # rarity is valid

    print(consumable[1] + "(x" + consumable[3] + ") ditambahkan ke database sementara.")
    consumable_data.append(consumable)
    return consumable_data
    


def rarityValid(text):
    # Spesifikasi : Mencecek apakah rarity valid, duh
    # KAMUS LOKAL LOKAL
    # ALGORITMA
    if text == "C" or text == "B" or text == "A" or text == "S":
        return True
    else:
        return False
