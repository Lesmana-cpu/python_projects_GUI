#operasi dan manipulasi str

#1. menyambung string (concatenate)

nama_pertama = 'L7'
nama_tengah = 'Ls689'

nama_akhir = nama_pertama + '' + nama_tengah
print(nama_akhir)


#2. menghitung panjang str
panjang = len(nama_akhir)
o = (f'panjang dari {nama_akhir} adalah = {panjang}')
print(type(o))
print(o)


#3. operator for str

#mengecek apakah ada karakter atau str di str

x = 'L7'
status = x in nama_akhir
print(f'apakah L7 ada di dalam {nama_akhir} (true/false) = {status}')

#versi NOT
x = 'L7'
status = x not in nama_akhir
print(f'apakah L7 tidak ada di dalam {nama_akhir} (true/false) = {status}')


#mengulang str
print(3*'astagfirullah ')
print('lailahaillallah ' * 3)


#indexing
print(f'index ke-0 from {nama_akhir} adalah = {nama_akhir[0]}')
print(f'index ke-5 from {nama_akhir} adalah = {nama_akhir[5]}')
print(f'index ke-(-2) from {nama_akhir} adalah = {nama_akhir[-2]}')
print(f'index ke-(-1) from {nama_akhir} adalah = {nama_akhir[-1]}')
print(f'index ke-(0:2) from {nama_akhir} adalah = {nama_akhir[0:2]}')   # arti 0:2 = 2 nya ga di itung
print(f'index ke-0,2,4,6 from {nama_akhir} adalah = {nama_akhir[0:8:2]}')  #start:stop:step


nama_pertama = 'L7'
nama_tengah = 'Ls689'

nama_akhir = nama_pertama + '' + nama_tengah
print(nama_akhir)

#item paling kecil
print(f'palling kecil{min(nama_akhir)}') 
                                                #sesuai abjad
#item paling besar
print(f'paling besar {max(nama_akhir)}')

ascii_code = ord('1')
print(f'asci code spasi adalah{str(ascii_code)}')
data = 777
print (f'char untuk ascii 777 adalah {chr(data)}')


#4. operator dalam bentuk method
date = 'lesmana 7777'
jumlah_7 = print(f'jumlah 7 = {date.count('7')}')