# Global dan local scope

nama_global = "suki" # <-- this is global variabel

# akses variabel global dalam fungsi
def fungsi1():
    print(f"menampilkan {nama_global}")
    
fungsi1()

# akses variabel global dalam loop

for i in range(1,6):
    print(f"loop ke {i} = {nama_global}")
    
# percabangan
if True:
    print(f"if True = {nama_global}")
    
    
def fungsi2():
    nama_local = "asep"
    print(nama_local)
fungsi2()
#print(nama_local) <-- ini tidak bisa

## contoh 1 penggunaan mengakses
def say() -> str :
    print(f"hai {name}")
# say() <-- ini akan error   
name = "karl"
say()


## contoh 2: merubah variabel global
angka = 0
name = "asep"
def ubah(nilai_baru, nama_baru):
    global angka # <-- fungsi ini mendapat akses merubah variabel global (angka)
    angka = nilai_baru
    global name 
    name = nama_baru
    
print(f"ini sebelum di rubah {angka,name}")
ubah(7, "ujang")
print(f"ini setelah di rubah {angka, name}")

##  contoh 3  <-- for sama if juga, bisa mengubah variabel global di local 
angka = 0
for i in range(0,5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy) 


if True:
    angka = 10
    angka_dummy = 10
    
print(angka)
print(angka)    