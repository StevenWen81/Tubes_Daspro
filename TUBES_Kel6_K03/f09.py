'''
MODUL F09 - Mengembalikan Gadget
v. 30 April 2021
Spesifikasi: Untuk user. Mengembalikan gadget dengan jumlah tertentu.
I.S. username orang yang sedang login, berbagai arr_full, lalu inputan
F.S. tuple berisi (1) gadget_return_history.csv yang baru,
(2) data perubahan untuk gadget.csv, dan
(3) data perubahan untuk gadget_borrow_history.csv, 
ketiganya untuk kemudian diaplikasikan saat save.
'''

import f99_analytics as f99

# KAMUS LOKAL
# Deklarasi variabel
# type arr_disp :
#   [
#       disp_n : int,
#       id_gadget : str,
#       nama_gadget : str,
#       jumlah_pinjam : int,
#       tanggal : str,
#       id_borrow : str
# ]
# type disp_tup :
#   (
#       arr_disp : arr_disp,
#       n_eff : int,
#       id_user : str
# )
# type pinjam :
#   [
#       id ; str
#       id_peminjam : str
#       id_gadget : str
#       tanggal_peminjaman : str
#       jumlah : str
#       is_returned : str
# ]
# type kembali :
#   [
#       id : str
#       id_peminjaman : str
#       tanggal_pengembalian : str
#       jumlah_pengembalian : str
# ]
# type gadget :
#   [
#       id : str
#       nama : str 
#       desc : str
#       jumlah : st
#       rarity : str
#       tahun : str
# ]

# Deklarasi fungsi dan prosedur
def kembalikan(user_data, gadget_data, gadget_borrow_history_data, gadget_return_history_data, logged_user):
    # Spesifikasi : Sesuai spesifikasi modul
    # I.S. arr2 dari berbagai csv, inputan user
    # F.S. print ke terminal, data file return, borrow, gadget
    # KAMUS LOKAL LOKAL
    # borrow_data : arr of pinjam
    # return_data : arr of kembali
    # gadget_data : arr of gadget
    # disp_tup : disp_tup
    # i, n_eff : int
    # id_user = str
    # ALGORITMA
    # Inisialisasi
    id_user = findIdFromUsername(user_data, logged_user)
    borrow_data = gadget_borrow_history_data
    return_data = gadget_return_history_data
    kembali = [
        "<0. id>",
        "<1. id_peminjaman>",
        "<2. tanggal_pengembalian>",
        "<3. jumlah_pengembalian>"
    ]
    disp_tup = fillArrDisp(borrow_data, gadget_data, id_user)

    # Pengecekan peminjaman
    n_eff = int(disp_tup[1])

    if not isMeminjam(id_user, borrow_data):
        print(logged_user + " sedang tidak meminjam gadget!")
        return ("NULL", "NULL", "NULL")
    else:  # is meminjam
        # Display ke terminal
        print("Wah, kamu " + logged_user + " belum mengembalikan:")

        for i in range(n_eff):
            disp_n = str(disp_tup[0][i][0])
            nama_gadget = str(disp_tup[0][i][2])
            jumlah_pinjam = str(disp_tup[0][i][3])
            print(disp_n + ". " + nama_gadget + ", sebanyak " + jumlah_pinjam + " buah.")

        kembali[0] = str(len(return_data))         
        no_pinjam = input("Masukkan nomor yang ingin dikembalikan: ")
        isNoPinjam = noPinjamValidity(no_pinjam, n_eff)
        while not isNoPinjam:
            print("Inputan tidak valid! Masukkan lagi.")
            no_pinjam = input("Masukkan nomor yang ingin dikembalikan: ")
            isNoPinjam = noPinjamValidity(no_pinjam, n_eff)

        idx = int(no_pinjam) - 1
        nama_gadget = str(disp_tup[0][idx][2])
        kembali[1] = disp_tup[0][idx][5] # id peminjaman

        kembali[2] = input("Masukkan tanggal pengembalian: ")  # tanggal_pengembalian
        while not tanggalValid(kembali[2]):
            print("Tanggal tidak valid! Masukkan dengan format DD/MM/YYYY")
            kembali[2] = input("Masukkan tanggal pengembalian: ")
        
        kembali[3] = input("Masukkan banyak " + nama_gadget + " yang dikembalikan: ")  # jumlah kembali
        jumlah_pinjam = disp_tup[0][idx][3]
        while not jumlahCukup(jumlah_pinjam, kembali[3]):
            # Display yang diatur jumlahCukup()
            kembali[3] = input("Masukkan banyak " + nama_gadget + " yang dikembalikan: ")
            jumlah_pinjam = disp_tup[0][idx][3]
        
        gadget_return_history_data.append(kembali)
        gadget_borrow_history_data = plusGlobalGadget(str(disp_tup[0][idx][1]), kembali[3], gadget_data)
        gadget_data = minGlobalBorrow(kembali[1], kembali[3], borrow_data)

        print("Item " + nama_gadget + "(x" + kembali[3] + ") dikembalikan.")
        print("Perubahan disimpan di database sementara.")
        return (gadget_return_history_data, gadget_borrow_history_data, gadget_data)


def noPinjamValidity(no_pinjam, n_eff):
    # SPEK : Cek kevalidan no pinjam
    # KAMUS LOKAL LOKAL
    # isNoPinjam : bool
    # no_pinjam : str
    # n_eff : int
    # ALGORITMA
    isNoPinjam = False

    if f99.charAreInt(no_pinjam):
        if int(no_pinjam) <= n_eff:
            isNoPinjam = True

    return isNoPinjam


def findIdFromUsername(user_data, logged_user):
    # SPEK: Mencari id dari data username
    # KAMUS LOKAL LOKAL
    # id_user : str
    # row : userline
    # ALGORITMA
    id_user = ""
    for row in user_data:
        if row[1] == logged_user:
            id_user = row[0]
    return id_user


def isMeminjam(id_user, borrow_data):
    # Spesifikasi : Mencari apakah logged_user sedang menunggak
    # KAMUS LOKAL LOKAL
    # isMeminjam : bool
    # i : int
    # borrow_data : arr of pinjam
    # id_user : str
    # ALGORITMA
    isMeminJam = False
    for i in range(1, (len(borrow_data) - 1)):
        if borrow_data[i][1] == id_user and borrow_data[i][5] == "False":
            isMeminJam = True
    return isMeminJam


def fillArrDisp(borrow_data, gadget_data, id_user):
    # Spesifikasi: Membuat arr data2 bermanfaat
    # I.S. borrow_data dan logged user
    # F.S. Nomor display, id gadget, nama gadget, jumlah pinjam, tanggal, id peminjaman
    # KAMUS LOKAL LOKAL
    # borrow_data : arr of pinjam
    # gadget_data : arr of gadget
    # arr_disp : arr_disp
    # i, disp_n, count : int
    # logged_user : str
    # ALGORITMA
    # Inisialisasi
    arr_disp = [[
        "<0. nomor display>", 
        "<1. id gadget>", 
        "<2. nama gadget>", 
        "<3. jumlah yang dipinjam>", 
        "<4. tanggal pengembalian>", 
        "<5. id peminjaman>"
    ] for i in range(1, (len(borrow_data)))]
    
    # Pengisian data
    count = 0
    for i in range(1, (len(borrow_data))):
        if borrow_data[i][1] == id_user and borrow_data[i][5] == "False":
            arr_disp[count][0] = count + 1
            arr_disp[count][1] = borrow_data[i][2]
            arr_disp[count][2] = gadgetName(borrow_data[i][2], gadget_data)
            arr_disp[count][3] = borrow_data[i][4]
            arr_disp[count][4] = borrow_data[i][3]
            arr_disp[count][5] = borrow_data[i][0]
            count += 1
    return (arr_disp, count)


def gadgetName(id_gadget, gadget_data):
    # Spesifikasi : Mencari nama gadget dengan id terspesifikasi. 
    # Oleh desain sistem, dijamin ada.
    # KAMUS LOKAL LOKAL
    # gagdet_data, gadget_data : arr of gadget
    # nama_gadget : str
    # i : int
    # ALGORITMA
    nama_gadget = "null"
    for i in range(1, (len(gadget_data))):
        if gadget_data[i][0] == id_gadget:
            nama_gadget = gadget_data[i][1]
    return nama_gadget


def tanggalValid(tanggal):
    # Spesifikasi : Mengecek apakah tanggal berformat DD/MM/YYYY, input bisa apapun.
    # KAMUS LOKAL LOKAL
    # arr_d_28, arr_d_29, arr_d_30, arr_d_31, arr_m_30, arr_m_31 : arr of str
    # d, m, y, tanggal : str
    # isValid : bool
    # ALGORITMA
    # Inisialisasi
    isValid = False
    arr_d_28 = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09",
        "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28"
    ]
    arr_d_29 = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09",
        "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"
    ]
    arr_d_30 = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09",
        "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
        "30"
    ]
    arr_d_31 = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09",
        "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
        "30", "31"
    ]
    arr_m_31 = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09",
        "10", "11", "12"
    ]
    arr_m_30 = ["04", "06", "09", "11"]
    arr_m_31 = ["01", "03", "05", "07", "08", "10", "12"]
    # Pengecekan tanggal
    if len(tanggal) == 10:
        d = tanggal[0:2]
        m = tanggal[3:5]
        y = tanggal[6:10]
        if f99.isTahun(y):
            if arr_d_31.count(d) > 0 and arr_m_31.count(m) > 0:  # Januari, Maret...
                isValid = True
            elif arr_d_30.count(d) > 0 and arr_m_30.count(m) > 0:  # April, Juni...
                isValid = True
            elif arr_d_29.count(d) > 0 and m == "02" and isKabisat(y): # Februari kabisat
                isValid = True
            elif arr_d_28.count(d) > 0 and m == "02" and not isKabisat(y):  # Februari non kabisat
                isValid = True
    return isValid


def isKabisat(tahun):
    # Spesifikasi: mencari apakah tahun kabisat, duh
    # KAMUS LOKAL LOKAL
    # tahun : int
    # ALGORITMA
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def jumlahCukup(jumlah_pinjam, jumlah_input):
    # Spesifikasi : Mencari apakah jumlah gadget yang dikembalikan > yang dipinjam
    # KAMUS LOKAL LOKAL
    # gadget_borrow_history_data : arr of pinjam
    # isCukup : bool
    # ALGORITMA
    isCukup = False
    if not f99.charAreInt(jumlah_input):
        print("Inputan tidak valid! Mohon masukkan lagi.")
    elif int(jumlah_pinjam) < int(jumlah_input):
        print("Inputan melebihi tunggakkan! Mohon masukkan lagi.")
    else:  # jumlah pinjam >= jumlah input
        isCukup = True
    return isCukup


def minGlobalBorrow(id_peminjaman, jumlah_input, borrow_data):
    # Spek : Megurangi jumlah tunggakan di file borrow, mengubah is_returned jika perlu
    # KAMUS LOKAL LOKAL
    # gadget_borrow_history_data, borrow_data : arr of pinjam
    # i : int
    # ALGORITMA
    for i in range(1, (len(borrow_data) - 1)):
        if borrow_data[i][0] == id_peminjaman:
            borrow_data[i][4] = str(int(borrow_data[i][4]) - int(jumlah_input))
            if borrow_data[i][4] == "0":
                borrow_data[i][5] = "true"
    
    return borrow_data


def plusGlobalGadget(id_gadget, jumlah_input, gadget_data):
    # Spek : Menambahkan barang yang sudah dikembalikan ke gadget.csv
    # KAMUS LOKAL LOKAL
    # gadget_data : arr of gadget
    # jumlah_input, id_gadget : str
    # ALGORITMA
    for i in range(1, (len(gadget_data) - 1)):
        if gadget_data[i][0] == id_gadget:
            gadget_data[i][3] = str(int(gadget_data[i][3]) + int(jumlah_input))
    return gadget_data
