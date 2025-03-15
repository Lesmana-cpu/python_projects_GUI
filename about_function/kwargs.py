'''**kwargs'''

def fungsi_kwargs(**kwargs):   # **kwargs <-- ini tipenya dictionary
    # print(kwargs)
    nama = kwargs["Nama"]  # <-- ini akan mencetak value dari key nya
    tinggi = kwargs["Tinggi"]
    berat = kwargs["Berat"]
    hobi = kwargs["Hobi"]
    print(f'{nama}\ntingginya = {tinggi}\nberatnya adalah = {berat}\nhobinya adalah {hobi}')
    
    # print(f'{kwargs["Nama"]}\ntingginya = {kwargs["Tinggi"]}\nberatnya adalah = {kwargs["Berat"]}\nhobinya adalah {kwargs["Nama"]}')  # <-- bisa juga gini
    
fungsi_kwargs(Nama = 'Ucep', Tinggi = 156, Berat = 38, Hobi = 'mancing')


# studi kasus
def math(*args, **kwargs):
    hasil_penjumlahan = 0
    if kwargs["operasi"] == "tambah":
        for jumlah in args:
            hasil_penjumlahan += jumlah
            
    elif kwargs["operasi"] == "kurang":
        for jumlah in args:
            hasil_penjumlahan -= jumlah
            
    elif kwargs["operasi"] == "kali":
        hasil_penjumlahan = 1
        for jumlah in args:
            hasil_penjumlahan *= jumlah
            
    elif kwargs["operasi"] == "tambah":
        hasil_penjumlahan = 1
        for jumlah in args:
            hasil_penjumlahan /= jumlah
            
    else:
        print('tidak ada operasinya')
            
    
    return hasil_penjumlahan

hasil = math(9, 7, 6, 6,1, operasi = "tambah")
print(hasil)

hasil = math(1,8,9,75,7, operasi = "kali")
print(hasil)