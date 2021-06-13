'''
MODUL 17 - Exit
v. 30 April 2021
Spesifikasi : Exit program secara umum
'''

import f15

# KAMUS LOKAL
# Deklarasi fungsi dan prosedur
def exit(isRunning, user_data,gadget_data,consumable_data,gadget_borrow_history_data,gadget_return_history_data,consumable_history_data):
   # Spesifikasi: sesuai spesifikasi modul
   # KAMUS LOKAL LOKAL
   # isRunning : bool
   # ALGORITMA
   while True:
      char = input("Apakah Anda mau menyimpan semua perubahan? (y/n): ")

      if char.upper().strip() == "Y":
         f15.save(user_data,gadget_data,consumable_data,gadget_borrow_history_data,gadget_return_history_data,consumable_history_data)
         print("Semua perubahan berhasil disimpan.")
         isRunning = False
         print("Terima kasih telah menggunakan Kantong Ajaib. ~Byeonara!\n")
         break

      elif char.upper().strip() == "N":
         print("Semua perubahan *tidak* disimpan, dan telah dihapus.")
         isRunning = False
         print("Terima kasih telah menggunakan Kantung Ajaib. ~Byeonara!\n")
         break

      else:  # Not y, Y, n, or N
         print("Input tidak valid! Silakan masukkan ulang.")

   return isRunning
