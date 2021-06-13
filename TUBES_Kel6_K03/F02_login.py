from csv_parser import *
from F14_load import *
from hashing import *

'''
# Dihilangkan karena ada fungsi "load"
file = csv_arr("user.csv")
for i in range(len(file)):
    file[i] = self_split(file[i],";")
'''    

def login(x):
    file = x
    terdaftar = False
    username = ""
    while terdaftar==False:
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        password = encrypt(password)
        
        for row in file:
            if username == row[1] and password == row[4]:
                print("Halo " + username + "! " + "Selamat datang di Kantong Ajaib.")
                terdaftar = True
        
        if terdaftar == False:
            print("Username dan/atau Password Anda Mungkin Salah!")
    return username
          
# login(nama_csv)