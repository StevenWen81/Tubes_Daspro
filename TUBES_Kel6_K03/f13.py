'''
MODUL F13 - MELIHAT RIWAYAT PENGAMBILAN CONSUMABLE
v. 30 April 2021
SPEK : Membaca dan mengout-putkan file riwayat pengambilan
I.S. array consumable_history_data
F.S. output data ke terminal, sesuai format
'''
import f99_analytics as f99
# KAMUS LOKAL
# Deklarasi Variabel
# type consumable_history :
#   [
#       id : str,
#       id_pengambil : str,
#       id_consumable : str,
#       tanggal_pengambilan : str,
#       jumlah : str
# ]
# type userline : 
#   [
#       id : str
#       username : str
#       nama : str
#       alamat : str
#       password : str
#       role : str
# ]
# type consumable :
#   [
#       id : str
#       nama : str 
#       desc : str
#       jumlah : st
#       rarity : str
# ]
# Deklarasi fungsi dan prosedur

def riwayatambil(user_data, consumable_data, consumable_history_data, logged_user):
    # SPEK : Sesuai modul
    # KAMUS LOKAL LOKAL
    # length, i : int
    # command : str
    # consumable_history_data : arr of consumable_history
    # user_data : arr of userline
    # consumable_data : arr of consumable
    # ALGORITMA
    if f99.isAdmin(logged_user):
        length = len(consumable_history_data)
        if length > 1:
            consumable_history_data = sortByDate(consumable_history_data, length)
        
        if length == 0:
            print("Data kosong! Tidak ada riwayat.")
        elif 0 < length <= 5:
            print("Data " + length + "x pengambilan terakhir:")
            for i in range((length - 1), -1, -1):
                printOneRow(i, user_data, consumable_data, consumable_history_data)
        else:  # length > 5
            while length > 1:
                if length < 5:
                    print("Data " + str(length) + "x pengambilan terakhir:")
                else:
                    print("Data 5x pengambilan terakhir:")

                length = printFiveRow(length, user_data, consumable_data, consumable_history_data)

                while length > 1:
                    command = input("Ingin melihat 5 entry sebelumnya? (y/n): ")
                    if command.strip().lower() == "n":
                        length = 0  # break loop besar
                        break  # break loop kecil
                    elif command.strip().lower() == "y":
                        break  # break loop kecil
                    else:  # command.strip().lower() == "y"
                        print("Inputan tidak valid! Silakan masukkan lagi.\n")
    else:
        print("Halt! Fungsi terbatas admin.")

        
def printOneRow(idx, user_data, consumable_data, consumable_history_data):
    # SPEK : Print 1 buah row, duh
    # KAMUS LOKAL LOKAL
    # idx : int
    # consumable_history_data : arr of consumable_history
    # user_data : arr of userline
    # consumable_data : arr of consumable
    # ALGORITMA
    print("ID Pengambilan: " + consumable_history_data[idx][0])
    print("Nama pengambil: " + getUsername(consumable_history_data[idx][1], user_data))
    print("Nama Consumable: " +  getConsumName(consumable_history_data[idx][2], consumable_data))
    print("Tanggal Pengambilan: " + consumable_history_data[idx][3])
    print("Jumlah: " + consumable_history_data[idx][4])
    print()


def getUsername(id, user_data):
    # SPEK : Mendapatkan username dari user_data dengan id user
    # KAMUS LOKAL LOKAL
    # username, id : str
    # user_data : arr of arr of str
    # ALGORTIMA
    username = ""
    for row in user_data:
        if row[0] == id:
            username = row[1]
    return username


def printFiveRow(length, user_data, consumable_data, consumable_history_data):
    # SPEK : Print 5 buah row, lalu return length - 5
    # KAMUS LOKAL LOKAL
    # length, i : int
    # consumable_history_data : arr of consumable_history
    # user_data : arr of userline
    # consumable_data : arr of consumable
    # ALGORITMA
    for i in range(0, 5):
            printOneRow((length - 1), user_data, consumable_data, consumable_history_data)
            length -= 1
            if length <= 1:  # EOP
                print("Data selesai.")
                break
    # EOP
    return length


def sortByDate(consumable_history_data, length):
    # SPEK : Mengurutkan list dari date terawal ke date terakhir
    # KAMUS LOKAL LOKAL
    # i, j, idx_max : int
    # t, t_max, m, m_max, ddmax : str
    # consumable_history_data, row_temp : arr of consumable_history
    # ALGORITMA
    # 1. Year sort
    for i in range(1, length - 1):
        # Find max idx
        idx_max = i
        t_max = consumable_history_data[i][3][6:10]
        for j in range(i + 1, length):
            t = consumable_history_data[j][3][6:10]
            if int(t) > int(t_max):
                idx_max = j
        # consumable_history_data[id_max] is now
        # max of consumable_history_data[i..length - 1]

        # Swap
        row_temp = consumable_history_data[idx_max]
        consumable_history_data[idx_max] = consumable_history_data[i]
        consumable_history_data[idx_max] = row_temp

    # 2. Month sort
    for i in range(1, length - 1):
        # Find max idx
        idx_max = i
        m_max = consumable_history_data[i][3][3:5]
        for j in range(i + 1, length):
            m = consumable_history_data[j][3][3:5]
            if int(m) > int(m_max):
                idx_max = j
        # consumable_history_data[id_max] is now
        # max of consumable_history_data[i..length - 1]

        # Swap
        row_temp = consumable_history_data[idx_max]
        consumable_history_data[idx_max] = consumable_history_data[i]
        consumable_history_data[idx_max] = row_temp

    # 3. Day sort
    for i in range(1, length - 1):
        # Find max idx
        idx_max = i
        m_max = consumable_history_data[i][3][0:2]
        for j in range(i + 1, length):
            m = consumable_history_data[j][3][0:2]
            if int(m) > int(m_max):
                idx_max = j
        # consumable_history_data[id_max] is now
        # max of consumable_history_data[i..length - 1]

        # Swap
        row_temp = consumable_history_data[idx_max]
        consumable_history_data[idx_max] = consumable_history_data[i]
        consumable_history_data[idx_max] = row_temp

    # Sorted based on date
    return consumable_history_data        


def getConsumName(id, consumable_data):
    # SPEK : Mendapatkan nama consumable dari consumable_data dengan id consumable
    # KAMUS LOKAL LOKAL
    # name, id : str
    # row : arr of str
    # consumable_data : arr of row
    # ALGORITMA
    name = ""
    for row in consumable_data:
        if row[0] == id:
            name = row[1]
    return name