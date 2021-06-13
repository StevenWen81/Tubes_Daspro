'''
Modul F07 - MENGUBAH JUMLAH GADGET ATAU CONSUMABLE PADA INVENTORY
1 Mei 2021
Spesifikasi : Mengubah jumlah gadget atau consumable pada sistem (akses: Admin)
'''

import f99_analytics as f99

# KAMUS LOKAL
# Deklarasi Variabel
# type gadget :
#   [   id : str
#       nama : str 
#       desc : str
#       jumlah : str
#       rarity : str
#       tahun : str ]
# type consumable :
#   [   id : str
#       nama : str 
#       desc : str
#       jumlah : st
#       rarity : str]
# type status :
#   [   jenis : str
#       idx : int   ]
# Deklarasi Fungsi
def ubahjumlah(gadget_data, consumable_data, logged_user, user_data):
    #Spesifikasi: Fungsi utama modul
    #KAMUS LOKAL LOKAL
    # id : str
    # gagdet_data, consumable_data: arr of arr of str
    # id_status : status
    #ALGORITMA
    if f99.isAdmin(logged_user, user_data) :
        id = input("Masukkan ID: ")
        id_status = Checkid(id, gadget_data, consumable_data)
        if id_status[0] == "Gadget": #untuk gadget
            ubahjumlahGadget(id_status, gadget_data)
        elif id_status[0] == "Consumable": #untuk consumable
            ubahjumlahConsumable(id_status, consumable_data)
        else: #id tidak valid
            print ("Tidak ada item dengan id tersebut!")
    else: #logged_user bukan admin
        print("Halt! Fungsi terbatas admin.")


def Checkid(id, gadget_data, consumable_data):
    #Spesifikasi: Menentukan kevalidan id, mencari indeks dengan id sesuai pada
    #data gadget atau consumable
    #KAMUS LOKAL LOKAL
    # id : str
    # gagdet_data, consumable_data: arr of arr of str
    # return_arr : status
    #ALGORITMA
    return_arr = ["Not Valid", 0] #inisiasi
    if id[0]== "G": 
        for i in range (len(gadget_data)):
            if id == gadget_data[i][0]:
                return_arr = ["Gadget", i] #id ditemukan di inventory gadget
    elif id[0]=="C":
        for i in range (len(consumable_data)):
            if id == consumable_data[i][0]:
                return_arr = ["Consumable", i] #id ditemukan di inventory consumable
    return return_arr
    
def ubahjumlahGadget (id_status, gadget_data):
    #Spesifikasi: Mengubah jumlah gadget pada inventory apabila jumlah akhir valid
    #KAMUS LOKAL LOKAL
    # id_status : status
    # idx, ubah, jumlah_i, jumlah_f: int
    # gadget_data: arr of gadget
    #ALGORITMA
    ubah = int(input("Masukkan Jumlah: "))
    idx=id_status[1]
    jumlah_i= int(gadget_data[idx][3])
    jumlah_f= jumlah_i + ubah
    if (jumlah_f>0):
        gadget_data[idx][3]=str(jumlah_f) #pengubahan jumlah item pada data gadget
        if (ubah>0):
            print(f"{ubah} {gadget_data[idx][1]} berhasil ditambahkan. Stok sekarang: {jumlah_f}")
        elif (ubah<0):
            print(f"{-1*ubah} {gadget_data[idx][1]} berhasil dibuang. Stok sekarang: {jumlah_f}")
    else: #jumlah final negatif (invalid)
        print(f"{-1*ubah} {gadget_data[idx][1]} gagal dibuang. Stok sekarang: {jumlah_i} (<{-1*ubah})")

def ubahjumlahConsumable (id_status, consumable_data):
    #Spesifikasi: Mengubah jumlah consumable pada inventory apabila jumlah akhir valid
    #KAMUS LOKAL LOKAL
    # id_status : status
    # idx, ubah, jumlah_i, jumlah_f: int
    # consumable_data: arr of consumable
    #ALGORITMA
    ubah = int(input("Masukkan Jumlah: "))
    idx=id_status[1]
    jumlah_i= int(consumable_data[idx][3])
    jumlah_f= jumlah_i + ubah
    if (jumlah_f>=0):
        consumable_data[idx][3]=str(jumlah_f) #pengubahan jumlah item pada data consumable
        if (ubah>=0):
            print(f"{ubah} {consumable_data[idx][1]} berhasil ditambahkan. Stok sekarang: {jumlah_f}")
        elif (ubah<0):
            print(f"{-1*ubah} {consumable_data[idx][1]} berhasil dibuang. Stok sekarang: {jumlah_f}")
    else: #jumlah final negatif (invalid)
        print(f"{-1*ubah} {consumable_data[idx][1]} gagal dibuang. Stok sekarang: {jumlah_i} (<{-1*ubah})")