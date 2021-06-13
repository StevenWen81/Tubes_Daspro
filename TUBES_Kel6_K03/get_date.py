import time

def tanggal_saat_ini():
    waktu = time.localtime()
    kalender = (time.asctime(waktu)) # format => hari bulan tgl jam:menit:detik tahun
    
    tahun = kalender[-4] + kalender[-3] + kalender[-2] + kalender[-1] # Untuk mengakali arr_kalender yang kurang kasus
    
    arr_kalender = []
    temp = ""
    
    for i in kalender:
        if i == " ":
            arr_kalender.append(temp)
            temp = ""
        else: 
            temp += str(i)
    # hasil arr_kalender adalah [hari, bulan, tanggal, jam:menit:detik] -> missing tahun

    tanggal = arr_kalender[3]
    
    bulan_str = arr_kalender[1]
    
    if bulan_str == "Jan":
        bulan_int = "01"
    elif bulan_str == "Feb":
        bulan_int = "02"
    elif bulan_str == "Mar":
        bulan_int = "03"
    elif bulan_str == "Apr":
        bulan_int = "04"
    elif bulan_str == "May":
        bulan_int = "05"
    elif bulan_str == "Jun":
        bulan_int = "06"
    elif bulan_str == "Jul":
        bulan_int = "07"
    elif bulan_str == "Aug":
        bulan_int = "08"
    elif bulan_str == "Sep":
        bulan_int = "09"
    elif bulan_str == "Oct":
        bulan_int = "10"
    elif bulan_str == "Nov":
        bulan_int = "11"
    else: #bulan_str == "Dec":
        bulan_int = "12"
    
    return (tanggal + "/" + bulan_int + "/" + tahun)