def f_kuadrat(angka):
    return angka**2

print(f_kuadrat(7))

# with lambda
# output = lambda arguments: expression
kuadrat = lambda angka:angka**5
print(kuadrat(5))

pangkat = lambda num,pow : num ** pow
print(pangkat(7, 9))


## kegunaan lambda

# sorting list biasa
data_list = ["asep", "suko", "Suki", "1", "ujang", "elang"] # <-- huruf besar (kapital) di dahulukan daripada huruf kecil
data_list.sort()
print(data_list)

# sorting with panjang
data_list = ["asep", "suko", "Suki", "1", "ujang", "elang"]
data_list.sort(key=len)
print(f"ini sort menggunakan len = {data_list}")


# sorting with panjang (function)
data_list = ["asep", "suko", "Suki", "1", "ujang", "elang"]
def panjang(data):
    return len(data)
data_list.sort(key=panjang)
print(f"ini sort menggunakan len (function) {data_list}")


# sort memakai lambda
data_list = ["asep", "suko", "Suki", "1", "ujang", "elang"]
data_list.sort(key=lambda nama:len(nama))
print(f"ini sort menggunakan len (lambda) {data_list}")

#kalo ingin memanggil lambda langsung
print((lambda p: p**2)(5))


# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_tujuh(angka):
    return angka < 7

data_angka_baru = list(filter(kurang_dari_tujuh, data_angka))
print(data_angka_baru)

# filter memakai lambda
#data_angka_baru_percobaan = list(filter(lambda x:x<7, data_angka))         <-- bebas, parameternya/argumentnya
#print(data_angka_percobaan)

data_angka_baru_part_2 = list(filter(lambda k_dari_seven:k_dari_seven <7, data_angka))
print(data_angka_baru_part_2)


# kasusu genap
data_genap = list(filter(lambda genap:(genap %2 ==  0), data_angka))
print(f"angka genap nya adalah {data_genap}")

# kasusu ganjil
data_ganjil = list(filter(lambda ganjil:(ganjil %2 != 0), data_angka))
print(f"angka ganjil nya adalah {data_ganjil}")

# kasusu kelipatan_3
data_kelipatan_3 = list(filter(lambda tree:(tree %3 == 0), data_angka))
print(f"angka kelipatan_3 nya adalah {data_kelipatan_3}")

# anonymouse function
# curryinng <-- haskell curry

def pangkat(angka,n):  # <-- fungsi biasa
    hasil = angka**n
    return hasil

hasil = pangkat(5,2)
print(f"hasil dari fungsi biasa = {hasil}")


# dengan currying
def pangkat(n):
    return lambda angka:angka**n

pangkat_3 = pangkat(3)
print(f"hasil menggunakan currying = {pangkat_3(7)}")

#or
pangkat_2 = pangkat(2)(5)
print(f"hasil menggunakan currying = {pangkat_2}")

#or
print(f"hasil menggunakan currying = {pangkat(4)(5)}\n\n")


# kebalikan untuk parameter pangkatnya
def pangkat(n):
    return lambda angka:n**angka

pangkat_3 = pangkat(3)
print(f"hasil menggunakan currying = {pangkat_3(7)}")

#or
pangkat_2 = pangkat(2)(5)
print(f"hasil menggunakan currying = {pangkat_2}")

#or
print(f"hasil menggunakan currying = {pangkat(4)(5)}")