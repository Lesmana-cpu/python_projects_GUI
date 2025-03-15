#                               '''*args'''

# kalo gini kan ribet dadak make [], makanya make *args
def fungsi_list(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'nama = {nama}\ntinggi = {tinggi}cm\nberat = {berat}kg')
    
fungsi_list(['asep', 172, 89])


print('\n\n')


# *args

def fungsi_with_args(*args):   # *args <-- ini jenis datanya tuple
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'nama = {nama}\ntinggi = {tinggi}cm\nberat = {berat}kg')
    
fungsi_with_args('joni', 156, 48)


# contoh pemakaiannya

def kali(*data):
    # data ini tipe nya tuple, jadi bisa di iterasikan
    output = 1
    
    for jumlah in data:
        output *= jumlah
    
    return output

hasil = kali(9, 7, 9, 5, 3, 3, 7)
print(hasil)



