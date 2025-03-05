#pengecekan dengan isx method
e = 'assalamualaikkum'
apakah_e_lower = e.islower()    #-> apakah e itu lower semua
apakah_e_upper = e.isupper()

print(str(apakah_e_lower))
print(apakah_e_upper)


huruf = 'astagfirullah'
angka_huruf = 'Lesmana777'
angka = '777'
space = '      \n' # ga boleh karakter / angka 
title = 'Hai Wtf'   # <-- cuma huruf awal yg gede  baru true

print('\n')

#isalpha() <-- untuk mengecek semuanya huruf
print(f'True or False {huruf} <-- huruf semua')
h = huruf.isalpha()
print(f'{h}\n')


#isalnum() <-- huruf dan angka
print(fr'True\False {angka_huruf} <-- angka dan huruf')
af = angka_huruf.isalnum()
print(f'{af} \n')


#isdecimal() <-- angka aja
print(fr'yang mana yang benar antara {angka} & {angka_huruf}  yang angka saja')
a = angka.isdecimal()
b = angka_huruf.isdecimal()
print(f'ini {angka} <-- {a}')
print(f'ini {angka_huruf} <-- {b}\n')

#isspace() <-- spase, tab, newline(n)
print(fr'apakah {space} mengandung spasi, tab, \n?')
s = space.isspace()
print(f'{s}\n')



#istitle() <-- semua di mulai dengan huruf besar
print(fr'True\False {title} <-- dimulai dengan huruf besar')
t = title.istitle()
print(f'{t}\n')



## ngecek komponen, startswith() & endswith()

#startswith("what's word?")
print('ini yang startswith()')
cek_start = "Lesmana  77".startswith('Lesmana')
f = str(cek_start)
print(cek_start)
print(f'{type(f)}\n')


#endswith("what's word?")
print('ini yang endswith')
cek_end = 'Lesmana 777 x'.endswith('x')
print(f'{cek_end}\n')



##penggabungan komponen, join(), split()

#join('masukkan variabel list nya')
pisah = ['Lesmana', 'Black', 'Arch', 'Linux']
print(pisah)

gabung = ','.join(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = '\n'.join(pisah)
print(gabung)

#split   <-- menjasi list lagi
gabung = 'Lesmana\nBlack\nArch\nLinux'
print(gabung.split('\n'))  # <-- menghilangka enter (\n)



##alokasi karakter rjust(), ljust(), center()

kanan = 'lesmana77'.rjust(20)
print(f'"{kanan}"')

kiri = 'lesmana77'.ljust(20)
print(f'"{kiri}"')

tengah = 'lesmana77'.center(20, '=')
print(f'"{tengah}"')


#kebalikannya <-- strip()
tengah = tengah.strip('=')
print(tengah)

kanan = kanan.strip()
print(kanan)