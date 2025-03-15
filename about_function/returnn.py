''' fungsi with return'''


# fungsi kuadrat
def kuadrat(x):
    hasil = x**2
    return hasil

y = kuadrat(5)
print(y)

print(kuadrat(9))


# contoh inputan
z = kuadrat(int(input('masukkan angkanya...')))
print(z)



# fungsi tambah
def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2


a = fungsi_tambah(3, 7)
print(a)

print(fungsi_tambah(7, 9))


# fungsi dengan return banyak
def operasi_math(angka_1, angka_2):
    kali = angka_1 * angka_2
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    bagi  =  angka_1 / angka_2
    
    return kali, tambah, kurang, bagi

k, t, ku, b = operasi_math(9, 7)

print(f'kali = {k}')
print(f'tambah = {t}')
print(f'kurang = {ku}')
print(f'bagi = {b}')



