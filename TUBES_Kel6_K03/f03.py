'''
Modul F03 - Pencarian Gadget Berdasarkan Rarity
1 Mei 2021
Spesifikasi: menampilkan semua gadget dengan rarity yang dimasukan pengguna (akses: Admin,User)
'''
# KAMUS LOKAL:
# Deklarasi Variabel
# type gadget :
#   [   id : str
#       nama : str 
#       desc : str
#       jumlah : str
#       rarity : str
#       tahun : str ]
# Deklarasi Fungsi
def carirarity(gadget_data):
    #Spesifikasi: fungsi utama modul
    #KAMUS LOKAL LOKAL
    #gadget_data: arr of arr of str
    #rarity: str
    #found : bool
    #ALGOTIMA
    rarity = input("Masukkan rarity: ") #Asumsi input pasti valid (C/B/A/S)
    print("\nHasil Pencarian:\n")
    found=False #inisiasi
    for i  in range (len(gadget_data)): 
        if gadget_data[i][4]==rarity: #pengecekan rarity sesuai input
            print("Nama\t\t: "+gadget_data[i][1])
            print("Deskripsi\t: "+gadget_data[i][2])
            print("Jumlah\t\t: "+gadget_data[i][3])
            print("Rarity\t\t: "+gadget_data[i][4])
            print("Tahun ditemukan : "+gadget_data[i][5])
            print()
            found=True
    if found==False: #rarity tidak ditemukan
        print(f"Tidak ditemukan gadget dengan rarity {rarity}.")
