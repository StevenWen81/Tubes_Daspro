def encrypt(sandi):
    hasil = []
    samar = ""
    
    for i in sandi:
        nilai = ord(i)
        hasil.append(nilai)
        nilai = ord(i)-1 # Digunakan agar tidak ada password yang sama dari input yg berbeda
        hasil.append(nilai)
        
        if ord(i)%2 == 0:
            nilai = ord(i)%10 # Digunakan agar tidak ada password yang sama dari input yang berbeda
            hasil.append(nilai)
        else:
            nilai = ord(i)//10 # Digunakan agar tidak ada password yang sama dari input yang berbeda
            hasil.append(nilai)
        
    for i in hasil:
        samar += str(i)
    
    return samar

'''
print(ord("n"))
print(encrypt("Ini Password 123#"))
print(chr(73))
print(chr(72))
'''

'''
I => 73723 => 73 72 3
n => 1101090 => 110 109 0
'''
