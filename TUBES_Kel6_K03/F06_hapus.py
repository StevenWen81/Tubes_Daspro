from csv_parser import *
from F14_load import *

def hapusitem(gadget_data,consumable_data):
    id_item = input("Masukan ID item: ")
    ada_id_item = False
    keputusan = ""
    nama_file = ""
    
    if id_item[0] == "G": # Untuk mengetahui file apa yang harus dibuka
        nama_file = "gadget.csv"

        file = gadget_data # Membuka file gadget karena input awal berupa "G"

        # Mengecek apakah terdapat ID inputan pengguna dalam database
        for row in file:
            if id_item == row[0]:
                ada_id_item = True
    
    if id_item[0] == "C": # Untuk mengetahui file apa yang harus dibuka
        nama_file = "consumable.csv"

        file = consumable_data # Membuka file consumable karena input awal berupa "C"

        # Mengecek apakah terdapat ID inputan pengguna dalam database
        for row in file:
            if id_item == row[0]:
                ada_id_item = True
            
    if ada_id_item == False: # ID yang diinput tidak valid atau tidak ada dalam database
        print("Tidak ada item dengan ID tersebut")
    
    if ada_id_item == True: # ID yang diinput terdapat dalam data base    
        for row in file:
            if id_item == row[0]:
                keputusan = input("Apakah anda yakin ingin menghapus " + row[1] + " (Y/N)? ")
        
        # Membuat data baru
        if keputusan.upper().strip() == "Y":
            print("Item telah berhasil dihapus dari database.")  
            new_database = []
            for i in file:
                new_database.append(i) # Menyalin isi CSV ke array baru
            for i in new_database:
                if id_item == i[0]:
                    new_database.remove(i) # Menghapus suatu baris sesuai dengan ID yang diinputkan pengguna
            
            # Mengirim data baru <zhillan>
            if nama_file == "gadget.csv":
                return (new_database, "gadget_data")
            elif nama_file == "consumable.csv":
                return (new_database, "consumable_data")
            else:
                return ("NULL", "NULL")                  
            
        elif keputusan.upper().strip() == "N":
            print("Item tidak jadi dihapus dari database.")   
            return ("NULL", "NULL")
        elif keputusan == "":
            keputusan = ""
            return ("NULL", "NULL")
        else:
            print("Input tidak valid")
            return ("NULL", "NULL")
        
        
# hapusitem()