# v.2 Mei 2021

def riwayat_pengembalian_gadget(gadget_return_history_data, gadget_borrow_history_data, gagdet_data):              # Program untuk melihat riwayat pengembalian gadget
    arr1 = gadget_return_history_data
    arr2 = gadget_borrow_history_data
    arr3 = gagdet_data
    riwayat(arr1, arr2, arr3)  
    del arr1[len(arr1) : len(arr1)-6 : -1]                      # Program akan menghilangkan 5 riwayat pengembalian gadget dari bawah untuk sementara
    if len(arr1) >= 2:                                          # Apabila masih ada riwayat yang belum ditampilkan, akan ditanya apakah ingin menampilkan lagi
        print('Apakah ingin menampilkan 5 riwayat lagi?')
        x = input()
        print('')
        if x == 'YA':                                           # Jika 'YA' program akan mengeluarkan riwayat lagi
            riwayat_pengembalian_gadget(arr1, arr2, arr3)
    else:                                                       # Apabila riwayat sudah ditampilkan semua, program akan berhenti
        print('Riwayat sudah ditampilkan semua.')               


def riwayat(arr1, arr2, arr3):                                  # Program untuk mengambil 5 riwayat pengembalian gadget yang paling baru
    N = len(arr1)
    X = []
    for k in range(N, N-5, -1):
        X += [arr1[N-1]] 
        N -= 1
        if N == 1:
            break
    M = sort_tgl(X)                                             # Program akan mengambil tanggal-tanggalnya
    for k in range(len(M)):                                     # Program akan mengeluarkan output nya satu persatu dari tanggal pengembalian yang paling baru
        indeks = M.index(max(M))
        output(X, arr2, arr3, indeks)
        M[indeks] = -999


def sort_tgl(X):                                                # Untuk membuat array yang berisikan tanggal pengembaliannya
    i = 0
    j = []
    N = len(X)
    for i in range(N):
        l = X[i][1]
        d = l[0:2]
        m = l[3:5]
        y = l[6:10]
        z = int(y+m+d)
        i += 1
        j.append(z)
    return j                                                    # Program mengembalikan array nya


def output(X, arr2, arr3, i):                                   # Program untuk mengoutput
    indeks = 0
    index = 0
    for j in range(len(arr2)):                                  # Untuk mencari nama pengambil dari riwayat peminjaman gadget
        if X[i][0] == arr2[j][0]:
            index = j
    for k in range(len(arr3)):                                  # Untuk mencari nama gadget dari inventori gadget
        if arr2[index][2] == arr3[k][0]:
            indeks = k
    print('ID Pengembalian      :',X[i][0])
    print('Nama Pengambil       :',arr2[index][1])
    print('Nama Gadget          :',arr3[indeks][1])
    print('Tanggal Pengembalian :',X[i][2])
    print('')
