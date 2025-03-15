from doctest import Example
from package_science import physics #, mth
from package_science.physics import potensial as pt
import package_science 

# hasil = mth.tambah(7,8,9,6)
# print(hasil)

gaya_p = physics.potensial(6,7)
print(f"gaya potensial = {gaya_p}")

gaya_p = pt(9,120)
print(f"gaya potensial = {gaya_p}")



# 2
import package_science  # <-- dari init

hasil = package_science.mth.tambah(2,6,7) 
hasil_2 = package_science.kali(9,7,5)

print(hasil)
print(hasil_2)


# 3
from package_science import *
hasil_bagi = contoh.mtk.bagi(100000, 5, 10,2)
print(hasil_bagi)
