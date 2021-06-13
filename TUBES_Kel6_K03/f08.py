# v.2 Mei 2021

def pinjam(gadget_data, gadget_borrow_history_data):                                                                                 # Program untuk meminjam gadget dari inventori
    ID = input('Masukkan ID item: ')   
    arr1 = gadget_data
    arr2 = gadget_borrow_history_data                                                             # Menginput ID gadget yang ingin dipinjam
    while True:
        if Cek_ID(arr1, ID) == True:
            if Cek_Pinjam(ID, arr2) == True:                                                        # Apabila gadget sedang dipinjam
                print('Gadget sedang dipinjam, silahkan pinjam gadget yang lain.')
                ID = input('Masukkan ID item: ')
            else:
                break
        else:                                                                                       # Apabila ID gadget tidak ada di inventori
            print('ID tidak valid.')
            ID = input('Masukkan ID item: ')
    Tgl = input('Tanggal peminjaman: ')                                                             # Menginput tanggal peminjaman
    while True:
        if Cek_Tgl(arr1, Tgl) == True:
            break
        else:                                                                                       # Apabila tanggal tidak valid
            print('Tanggal tidak valid.')
            Tgl = input('Tanggal peminjaman: ')
    Jml = input('Jumlah peminjaman: ')                                                              # Menginput jumlah yang ingin dipinjam
    while True:
        if Cek_Jml(arr1, ID, Jml) != True:                                                          # Apabila jumlah yang ingin dipinjam tidak mencukupi
            print('Jumlah tidak mencukupi.')
            Jml = input('Jumlah peminjaman: ')
        else:                                                                                       # Jika sudah benar mengoutput
            i = 0
            N = (len(arr1))
            for i in range(N):
                if ID != arr1[i][0]:
                    i+1
                elif ID == arr1[i][0]:                    
                    print('Item ' + arr1[i][1] + '(x' + Jml + ') berhasil dipinjam!')
            break

    arr_baru(arr2, ID, Tgl, Jml)
    # arr2 (gadget_borrow_history_data) sudah di-update                                                                                # Menggabungkan pinjaman gadget kedalam array riwayat peminjaman gadget
    return arr2
    
      
def Cek_ID(arr, ID):                                                                                            # Program untuk mengecek ID ada atau tidak di inventori
    i = 0
    N = (len(arr))
    for i in range(N):
        if ID != arr[i][0]:
            i += 1
        elif ID == arr[i][0]:                                                                                   # Apabila ada akan mengembalikan True
            return True

    
def Cek_Tgl(arr, Tgl):                                                                                          # Program untuk mengecek input tanggal valid atau tidak
    arr_d_28 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
     "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
    arr_d_29 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
     "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
    arr_d_30 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
     "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
    arr_d_31 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
     "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    arr_m_30 = ["04", "06", "09", "11"]
    arr_m_31 = ["01", "03", "05", "07", "08", "10", "12"]
    if (len(Tgl)) == 10:
        d = Tgl[0:2]
        m = Tgl[3:5]
        y = int(Tgl[6:10])
        if isKabisat(y) and m == '02' and arr_d_29.count(d) > 0:                                                # Apabila tahun kabisat dan bulan februari
            return True
        elif isKabisat(y) == False and m == '02' and arr_d_28.count(d) > 0:                                     # Apabila bukan tahun kabisat dan bulan februari
            return True
        elif arr_m_30.count(m) > 0 and arr_d_30.count(d) > 0:                                                   # Apabila bukan tahun kabisat dan bulan yang 30 hari
            return True
        elif arr_m_31.count(m) > 0 and arr_d_31.count(d) > 0:                                                   # Apabila bukan tahun kabisat dan bulan yang 31 hari
            return True
    else:                                                                                                       # Apabila bukan dari yang diatas
        return False                                                                                           


def isKabisat(tahun):                                                                                           # Program untuk mencari tahu apakah tahun inputan merupakan tahun kabisat
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


def Cek_Jml(arr, ID, Jml):                                                                                      # Program untuk mengecek apakah jumlah gadget yang ingin dipinjam mencukupi
    i = 0
    N = (len(arr))
    for i in range(N):
        if ID != arr[i][0]:
            i += 1
        elif ID == arr[i][0]:
            if (int(arr[i][3]) - int(Jml)) >= 0:
                return True                                                                                     # Apabila cukup akan mengembalikan True


def Cek_Pinjam(ID, arr):                                                                                        # Program untuk mengecek apakah gadget sedang dipinjam
    i = 1 
    N = (len(arr))
    for i in range(N):
        if ID != arr[i][2]:
            i += 1
        elif ID == arr[i][2]:
            return True                                                                                         # Apabila iya akan mengembalikan True


def arr_baru(arr2, ID, Tgl, Jml):                                                                               # Program yang membuat array baru untuk entry riwayat peminjaman gadget
    N = len(arr2)
    X = [str(N+1), 'User', str(ID), str(Tgl), str(Jml), 'False']
    arr2.append(X)


