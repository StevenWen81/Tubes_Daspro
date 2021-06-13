from csv_parser import *

def load(awal_folder, x):
    if x == "user_csv":
        user_data = awal_folder + "/" + "user.csv"
        file = csv_arr(user_data)
        for i in range(len(file)):
            file[i] = self_split(file[i],";") # Membuat ArrayOfArray dengan ";" sebagai pemisah isi ArrayOfArray

    elif x == "gadget_csv":
        gadget_data = awal_folder + "/" + "gadget.csv"
        file = csv_arr(gadget_data)
        for i in range(len(file)):
            file[i] = self_split(file[i],";") # Membuat ArrayOfArray dengan ";" sebagai pemisah isi ArrayOfArray

    elif x == "consumable_csv":
        consumable_data = awal_folder + "/" + "consumable.csv"
        file = csv_arr(consumable_data)
        for i in range(len(file)):
            file[i] = self_split(file[i],";") # Membuat ArrayOfArray dengan ";" sebagai pemisah isi ArrayOfArray

    elif x == "consumable_history_csv":
        consumable_history_data = awal_folder + "/" + "consumable_history.csv"
        file = csv_arr(consumable_history_data)
        for i in range(len(file)):
            file[i] = self_split(file[i],";") # Membuat ArrayOfArray dengan ";" sebagai pemisah isi ArrayOfArray

    elif x == "gadget_borrow_history_csv":
        gadget_borrow_history_data = awal_folder + "/" + "gadget_borrow_history.csv"
        file = csv_arr(gadget_borrow_history_data)
        for i in range(len(file)):
            file[i] = self_split(file[i],";") # Membuat ArrayOfArray dengan ";" sebagai pemisah isi ArrayOfArray

    elif x == "gadget_return_history_csv":
        gadget_return_history_data = awal_folder + "/" + "gadget_return_history.csv"
        file = csv_arr(gadget_return_history_data)
        for i in range(len(file)):
            file[i] = self_split(file[i],";") # Membuat ArrayOfArray dengan ";" sebagai pemisah isi ArrayOfArray

    else: # file csv diluar yang ditentukan -> salah karena tidak ada
        return ("Nama File yang Anda Masukkan Tidak Ada Dalam Folder CSV")

    return file

'''
file = load("gakada_csv")
print(file)
'''