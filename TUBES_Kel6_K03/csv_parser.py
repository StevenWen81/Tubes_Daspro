def self_split(stri,token):
    result = list()
    temp = ""
    
    for i in range(len(stri)):
        if stri[i] == token:
            result.append(temp)
            temp = ""
        else:
            temp += (stri[i])
            
    result.append(temp)
    return result
    

def csv_arr(csv):
    file = open(csv, "r")
    result = list()
    
    while True:
        result_temp = file.readline().strip()
        
        if not result_temp:
            break
        
        result.append(result_temp)
    
    return result

def arr_csv(arr):
    result = "\n".join(arr)
    return result

def combine_str(arr):
    for i in range(len(arr)):
        arr[i] = ";".join(arr[i])

'''
Note:
Untuk mengubah dari csv ke arr, gunakan csv_arr lalu dilanjutkan dengan self_split
Untuk mengubah dari arr ke csv, gunakan combine_str lalu dilanjutkan dengan arr_csv
'''

'''
Uji coba:
arr = [["1","2","3"],["2","4"]]
combine_str(arr)
print(arr)
print(arr_csv(arr))
'''