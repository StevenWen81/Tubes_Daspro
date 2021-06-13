'''
Modul F15 - SAVE DATA
1 Mei 2021
Spesifikasi: Penyimpanan semua file setelah dilakukan perubahan ke suatu folder. (akses: admin, user)
'''
import os
# KAMUS LOKAL
# Deklarasi Variabel
# type gadget_borrow_history:
#   [   id          : str
#       id_peminjam : str 
#       Id_gadget   : str
#       tanggal     : str
#       jumlah      : str
#       is_returned : str ]
# type gadget_return_history:
#   [   id          : str
#       id_peminjam : str 
#       tanggal     : str ]
# type consumable_history:
#   [   id          : str
#       id_peminjam : str 
#       Id_gadget   : str
#       tanggal     : str
#       jumlah      : str ]
# type gadget :
#   [   id     : str
#       nama   : str 
#       desc   : str
#       jumlah : str
#       rarity : str
#       tahun  : str ]
# type user : 
#   [   id       : str
#       username : str
#       nama     : str
#       alamat   : str
#       password : str
#       role     : str  ]
# type consumable : 
#   [   id : str
#       nama : str 
#       desc : str
#       jumlah : st
#       rarity : str  ]
# Deklarasi Fungsi
def save(user_data,gadget_data,consumable_data,gadget_borrow_history_data,gadget_return_history_data,consumable_history_data):
    # Spesifikasi : Fungsi utama modul
    # KAMUS LOKAL LOKAL
    # all_str, all_file : arr of str
    # folder: str
    # user_data = user
    # gadget _data = gadget
    # consumable_data = consumable
    # gadget_borrow_history_data = gadget_borrow_history
    # gadget_return_history_data = gadget_return_history
    # consumable_history _data = consumable_history
    # ALGORITMA
    all_str = [data_str(user_data),data_str(gadget_data),data_str(consumable_data),data_str(gadget_borrow_history_data),data_str(gadget_return_history_data),data_str(consumable_history_data)]
    all_file= ["user.csv","gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable_history.csv"]
    folder = input("Masukkan nama folder penyimpanan: ") #input nama folder
    if folder not in os.listdir(): 
        os.mkdir(folder) #pembuatan folder bila perlu
    for i in range (len(all_file)): #penyimpanan semua file dalam folder
        savefile(all_file[i],folder,all_str[i])
    print ("Saving...")
    print (f"Data telah disimpan pada folder {folder}!")

def savefile(file, folder, string):
    #Spesifikasi: Menyimpan file dalam folder
    #KAMUS LOKAL LOKAL
    # file, folder, string: str
    #ALGORITMA
    if file in os.listdir(folder):
        os.remove(folder+'/'+file)
    f = open(folder+"/"+file, "w")
    f.write(string)
    f.close()

def data_str(data):
    #Spesifikasi: Merubah arr of arr of str menjadi str sesuai format csv
    #KAMUS LOKAL LOKAL
    # string : str
    # data : arr of arr of str
    #ALGORITMA
    string = ""
    for arr in data:
        string +=";".join(arr)
        string += "\n"
    return string