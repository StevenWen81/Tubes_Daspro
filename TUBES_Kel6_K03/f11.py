'''
Modul F11 - MELIHAT RIWAYAT PEMINJAMAN GADGET
1 Mei 2021
Spesifikasi : Melihat riwayat peminjaman gadget yang telah terurut berdasarkan tanggal
peminjaman dari yang paling baru (akses: Admin)
'''
import f99_analytics as f99
from datetime import datetime

# KAMUS LOKAL
# Deklarasi Variabel
# type gadget_borrow_history:
#   [   id          : str
#       id_peminjam : str 
#       Id_gadget   : str
#       tanggal     : str
#       jumlah      : str
#       is_returned : str ]
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
# Deklarasi Fungsi
def riwayatpinjam (gadget_borrow_history_data,logged_user,user_data,gadget_data):
    # Spesifikasi : Fungsi utama modul
    # KAMUS LOKAL LOKAL
    # header = arr of str
    # lanjut = str
    # idx = int
    # finish = bool
    # gadget_borrow_history_data, sorted_tanggal = gadget_borrow_history
    # ALGORITMA
    if f99.isAdmin(logged_user, user_data) :
        header = gadget_borrow_history_data.pop(0) #pengeluaran arr header dari arr of arr
        sorted_tanggal = sorted(gadget_borrow_history_data,key=lambda date: datetime.strptime(date[3],'%d/%m/%Y'),reverse=True)
        gadget_borrow_history_data.insert(0,header) #pengembalian header agar tidak mengubah variabel global
        finish = False #inisiasi
        idx=-1 # inisiasi
        while not finish:
            for i in range (5): #pengeluaran 5 entry
                idx += 1
                if idx >= len(sorted_tanggal): 
                    finish = True
                else:
                    print("\nID Peminjaman\t\t:"+sorted_tanggal[idx][0])
                    print("Nama Pengambil\t\t:"+carinama(sorted_tanggal[idx][1],user_data))
                    print("Nama Gadget\t\t:"+carigadget(sorted_tanggal[idx][2],gadget_data))
                    print("Tanggal Peminjaman\t:"+sorted_tanggal[idx][3])
                    print("Jumlah\t\t\t:"+sorted_tanggal[idx][4])
            while not finish:
                if idx < len(sorted_tanggal):
                    lanjut = input("\nLihat entry selanjutnya? (Y/N) :") #opsi mengeluarkan 5 entry berikutnya
                    if lanjut.strip().capitalize() == "N": 
                        finish = True 
                    elif lanjut.strip().capitalize()  == "Y":
                        break
                    else: print ("input tidak sesuai!")
    else: #logged_user bukan admin
        print("Halt! Fungsi terbatas admin.")


def carinama (id,user_data):
    # Spesifikasi: Menerima input id dan mengeluarkan nama dengan id tersebut
    # KAMUS LOKAL LOKAL
    # user_data : arr of user
    # nama : str
    # ALGORITMA
    for i in range (len(user_data)):
        if id == user_data[i][0]:
            nama = user_data[i][1]
            return nama

def carigadget (id,gadget_data):
    # Spesifikasi: Menerima input id dan mengeluarkan gadget dengan id tersebut
    # KAMUS LOKAL LOKAL
    # user_data : arr of user
    # gadget : str
    # ALGORITMA
    for i in range (len(gadget_data)):
        if id == gadget_data[i][0]:
            gadget = gadget_data[i][1]
            return gadget


