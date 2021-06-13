from csv_parser import *
from get_date import *
from F14_load import *

def minta(x):
    ambil = False
    ada_di_database = False
    jumlah_valid = False
    flag_input = True

    while flag_input == True:
        try:
            id_item = input("Masukan ID item: ")
            jumlah = int(input("Jumlah: "))
            print("Tanggal permintaan: " + tanggal_saat_ini())
            flag_input = False

        except ValueError:
            print("Input jumlah harus integer")

    nama_file = "consumable.csv"
    file = x

    if int(jumlah) <= 0:
        print("Jumlah permintaan minimal adalah 1")
    
    if int(jumlah) > 0:
        jumlah_valid = True
    
    # Mengecek apakah ID yang diinput terdapat dalam database atau tidak
    for row in file:
        if id_item == row[0]:
            ada_di_database = True    
    
    if ada_di_database == False:
        print("Tidak ada item dengan ID tersebut")
        
    if (ada_di_database == True) and (jumlah_valid == True):
        # Memperbarui data base    
        new_database = []
        for i in file:
            new_database.append(i)
        for i in new_database:
            if id_item == i[0]:
                if int(i[3]) - int(jumlah) >= 0: # Apabila masih terdapat cukup item di database
                    i[3] = int(i[3]) - int(jumlah)
                    i[3] = str(i[3])
                    ambil = True
                if int(i[3]) - int(jumlah) < 0: # Jumlah item di database tidak boleh minus
                    print("Item tidak mencukupi permintaan")
                    ambil = False
        
        # Mengirim data baru <zhillan>
        
        
        if ambil == True:
            for row in file:
                if id_item == row[0]:
                    print("Item " + str(row[1]) + " (x" + str(jumlah) + ") " + "telah berhasil diambil!")
        return new_database

    else:
        return "NULL"
                
                
# minta()
