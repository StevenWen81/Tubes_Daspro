'''
PROGRAM KANTONG AJAIB IF1201 K-03 Kel. 6
v. 25 April 2021

16520193 Zhillan Attarizal Rezyarifin
16520203 Steven
16520353 Tubagus Baraka Kautsar S.
16520413 Jonathan

Spesifikasi : Program manajemen repository kantong ajaib Doramonangis
'''
# Dilakukan pemberian nama berulang pada import agar memudahkan penyamaan nama file, jika nanti diubah2
# Tidak digunakan "*" agar mencegah collision dan memudahkan pencarian dari modul manakah suatu fungsi
import f01
import F02_login as f02
import f03
import f04
import f05
import F06_hapus as f06
import f07
import f08
import f09
import F10_minta_consumable as f10
import f11
import f12
import f13
import F14_load as f14
import f15
import f16
import f17 
import f99_analytics as f99
import get_date, argparse, time

# KAMUS
# Deklarasi variabel
# logged_user : str
# isNotLoggedIn, isRunning : bool
# user_data, gadget_data, consumable_data, consumable_history_data,
# gadget_borrow_history_data, gadget_return_history_data : arr of arr of str

# Deklarasi fungsi dan prosedur
def displayOptions(command):
    # Spek : menampilkan semua opsi
    # KAMUS LOKAL
    # command : str
    # user_data, gadget_data, consumable_data, consumable_history_data,
    # gadget_borrow_history data, gadget_return_history_data, new_user, 
    # new_gadget, new_consum, new_consum_hist, new_gadget_borr, 
    # new_gadget_ret : arr of arr of str
    # ALGORITMA
    # Initialisasi data global agar dapat dipakai oleh fungsi
    global logged_user
    global isRunning
    global user_data
    global gadget_data
    global consumable_data
    global consumable_history_data
    global gadget_borrow_history_data
    global gadget_return_history_data

    # Eksekusi fungsi
    if command == "register":
        new_user = f01.register(user_data, logged_user)
        if new_user != "notAdmin":
            updateGlobal(new_user, "user_data")

    elif command == "login":
        logged_user = f02.login(user_data)

    elif command == "carirarity":
        f03.carirarity(gadget_data)

    elif command == "caritahun":
        f04.cari_gadget_tahun(gadget_data)

    elif command == "tambahitem":
        tup_f05 = f05.tambahitem(gadget_data, consumable_data, user_data, logged_user)
        if str(tup_f05[0]) != "null" and str(tup_f05[1]) == "null":  # Gadget
            updateGlobal(tup_f05[0], "gadget_data")
        elif str(tup_f05[0]) == "null" and str(tup_f05[1]) != "null":
            updateGlobal(tup_f05[1], "consumable_data")
    
    elif command == "hapusitem":
        tup_06 = f06.hapusitem(gadget_data, consumable_data)
        if tup_06[0] != "NULL":
            updateGlobal(tup_06[0], tup_06[1])  # data baru, jenis data
    
    elif command == "ubahjumlah":
        f07.ubahjumlah(gadget_data, consumable_data, logged_user, user_data)
    
    elif command == "pinjam":
        new_data = f08.pinjam(gadget_data, gadget_borrow_history_data)
        updateGlobal(new_data, "gadget_borrow_history_data")
    
    elif command == "kembalikan":
        tup_09 = f09.kembalikan(user_data, gadget_data, gadget_borrow_history_data, gadget_return_history_data, logged_user)
        if tup_09[0] != "NULL":
            updateGlobal(tup_09[0], "gadget_return_history_data")
            updateGlobal(tup_09[1], "gadget_borrow_history_data")
            updateGlobal(tup_09[2], "gadget_data")
    
    elif command == "minta":
        new_array = f10.minta(consumable_data)
        if new_array != "NULL":
            updateGlobal(new_array, "consumable_data")
    
    elif command == "riwayatpinjam":
        f11.riwayatpinjam(gadget_borrow_history_data,logged_user,user_data,gadget_data)
    
    elif command == "riwayatkembali":
        f12.riwayat_pengembalian_gadget(gadget_return_history_data, gadget_borrow_history_data, gadget_data)
    
    elif command == "riwayatambil":
        f13.riwayatambil(user_data, consumable_data, consumable_history_data, logged_user)
    
    elif command == "save":
        f15.save(user_data,gadget_data,consumable_data,gadget_borrow_history_data,gadget_return_history_data,consumable_history_data)
    
    elif command == "help":
        f16.help()
    
    elif command == "exit":
        isRunning = f17.exit(isRunning, user_data,gadget_data,consumable_data,gadget_borrow_history_data,gadget_return_history_data,consumable_history_data)
    
    else:  # Tidak ada yang cocok
        print("Perintah tidak valid! Ketik 'help' untuk bantuan.")


def displayDoramonangis():
    # Spek : Meng-outputkan ascii art Doramonangis
    # KAMUS LOKAL
    # f : seqfile of str
    # line : str
    # ALGORITMA
    f = open("doraemon.txt", "r")
    while True:
        line = f.readline().replace("\n", "")
        print(line)
        if not line:
            break
    f.close()


def updateGlobal(new_arr, arr_type):
    # Spek : menerima output modul2 dan mengupdate variabel global
    # KAMUS LOKAL
    # ALGORITMA
    # Initialisasi data global agar dapat dipakai oleh fungsi
    global user_data
    global gadget_data
    global consumable_data
    global consumable_history_data
    global gadget_borrow_history_data
    global gadget_return_history_data
    # Mengupdate dengan input
    if arr_type == "user_data":
        user_data = new_arr
    elif arr_type == "gadget_data":
        gadget_data = new_arr
    elif arr_type == "consumable_data":
        consumable_data = new_arr
    elif arr_type == "consumable_history_data":
        consumable_history_data = new_arr
    elif arr_type == "gadget_borrow_history_data":
        gadget_borrow_history_data = new_arr
    else:  # arr_type == "gadget_return_history_data"
        gadget_return_history_data = arr_type

# ALGORITMA PROGRAM UTAMA
isLoaded = False
# Fungsi load pertama dengan argparse
parser = argparse.ArgumentParser()
parser.add_argument("folder", type=str)

args = parser.parse_args()
hasil = args.folder

isLoaded = True
displayDoramonangis()
repeat_times = 3
while (repeat_times != 0):
    print("Loading...") # melakukan pengulangan pada titik-titik sehingga terlihat seperti loading asli
    repeat_times -= 1
    time.sleep(0.5) # melakukan delay pada output titik-titik sehingga terlihat seperti loading asli
print("Folder " + hasil + " telah berhasil di load")

# Deklarasi variabel GLOBAL
logged_user = "<NULL>"
isRunning = True

awal_csv = hasil + "/"
user_data = f14.load(awal_csv, "user_csv")
gadget_data = f14.load(awal_csv, "gadget_csv")
consumable_data = f14.load(awal_csv, "consumable_csv")
consumable_history_data = f14.load(awal_csv, "consumable_history_csv")
gadget_borrow_history_data = f14.load(awal_csv, "gadget_borrow_history_csv")
gadget_return_history_data = f14.load(awal_csv, "gadget_return_history_csv")

if isLoaded:
    print("\nPROGRAM KANTONG AJAIB IF1201 K-03 Kel. 6.\n2021. All rights not reserved.\n")
    # Login pertama
    logged_user = f02.login(user_data)
    # Loop display dan akses modul2
    while isRunning:
        if f99.isAdmin(logged_user, user_data):
            print("\nPerintah aku, master " + logged_user + "~!")
        else:  # Not admin
            print("\nAda yang bisa dibantu, " + logged_user + "?")
        command = input(">>> ")
        displayOptions(command.lower().strip(" "))
else:  # not loaded
    print("Program berakhir.")

# Untuk memulai: ketik ke terminal, "python kantongajaib.py 2021-04-25"