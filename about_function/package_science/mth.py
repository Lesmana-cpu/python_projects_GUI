# module matematika

def tambah(*angka):
    hasil = 0
    for data in angka:
        hasil += data
    return hasil

def kali(*angka_2):
    hasil_2 = 1
    for data_2 in angka_2:
        hasil_2 *= data_2
    return hasil_2 

def pangkat(n:int) -> int:
    return lambda angka:angka**n