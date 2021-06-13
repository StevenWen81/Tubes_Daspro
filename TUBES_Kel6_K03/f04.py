from F14_load import *

def cari_gadget_tahun(x):
    arr = x                                                                # Program untuk mencari gadget berdasarkan tahun ditemukan
    thn = input('Masukkan tahun: ')                                                     # Menginput tahun gadget
    kat = input('Masukkan kategori: ')                                                  # Menginput daerah tahun yang dicari
    kategori(arr, thn, kat)

def kategori(arr, thn, kat): 
    a = 0                                                                               # Program untuk mencari kategori yang diinginkan
    N = (len(arr))
    print('')
    print('Hasil pencarian:')
    for i in range(1, N):
        if kat == '=':                                                                  # Apabila gadget yang diinginkan sama dengan tahun yang diinginkan
            if arr[i][5] == thn:
                output(arr,i)
                i += 1
                a += 1
            else:
                i += 1
        if kat == '>':                                                                  # Apabila gadget yang diinginkan lebih baru dari tahun yang diinginkan
            if arr[i][5] > thn:
                output(arr,i)
                i += 1
                a += 1
            else:
                i += 1
        if kat == '<':
            if arr[i][5] < thn:                                                         # Apabila gadget yang diinginkan lebih lama dari tahun yang diinginkan
                output(arr,i)
                i += 1
                a += 1
            else:
                i += 1
        if kat == '>=':                                                                 # Apabila gadget yang diinginkan lebih baru dan sama dengan tahun yang diinginkan
            if arr[i][5] >= thn:
                output(arr,i)
                i += 1
                a += 1
            else:
                i += 1
        if kat == '<=':                                                                 # Apabila gadget yang diinginkan lebih lama dan sama dengan tahun yang diinginkan
            if arr[i][5] <= thn:
                output(arr,i)
                i += 1
                a += 1
            else:
                i += 1
    if a <= 0:
        print('Gadget tidak ditemukan.')                                                # Apabila gadget tidak ditemukan dari tahun dan kategori yang diinginkan

def output(x,i):                                                                        # Program untuk mengeluarkan output
    print('')
    print('Nama:',x[i][1])
    print('Deskripsi:',x[i][2])
    print('Jumlah:',x[i][3],'buah')
    print('Rarity:',x[i][4])
    print('Tahun Ditemukan:',x[i][5])