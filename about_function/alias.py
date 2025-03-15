from matematika import tambah as add
from matematika import pangkat as p
import matematika as math # <-- dari ini bisa juga

hasil_tambah = add(1,4,6,7,4)
print(f"hasil tambah adalah = {hasil_tambah}")

hasil_kali = math.kali(1,4,6,7,4)
print(f"hasil kali adalah = {hasil_kali}")

hasil_pangkat = p(2)
print(f"hasil pangkat adalah = {hasil_pangkat(3)}")