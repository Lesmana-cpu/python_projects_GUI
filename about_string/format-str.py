# format

# contoh generic

#string


nama = 'Lesmana 777'
format_str = f'halo bos {nama}\n'
print(format_str)


#boolean
bole = True
bolee = f'bolean = {bole}'
print(bolee)
print(f'{type(bolee)}\n')


#angka
angka = 779.7
angka_keren = f'angka keren = {angka}'
print(angka_keren)
print(f'{type(angka_keren)}\n')

#bilangan bulat
number = 7
format_int = f'bilangan bulat = {number:d}'   # :d <-- ngecek hanya integer
print(format_int)
print(f'{type(format_int)}\n')

#bilangan ribuan (,)
no = 77770
ribu = f'ribuan = {no:,}'  # :, <-- nambahin ,
print(ribu)
print(f'{type(ribu)}\n')

#bilangan decimal
decimal = 779.37464
decimal_keren = f'decimal  = {decimal:.2f}'  # :.2f <-- mau berapa banyak angka  yang di tampilin di belakang "." (f > float)
print(decimal_keren)
print(f'{type(decimal_keren)}\n')

#menampilkan leading zero
decimel = 779.37464
decimel_keren = f'decimel  = {decimel:08.2f}'  # :.2f <-- mau berapa banyak angka yang di tampilin di belakang "." (f > float), :0 nya nampilin mau berapa yang di cetak, ('.' di itung juga)
print(decimel_keren)
print(f'{type(decimel_keren)}\n')

#menampilkan tanda + atau -
minus = -3
plus = 9.789
format_minus = f'minus = {minus:+d}'
format_plus = f'plus = {plus:+.2f}'
print(f'{format_minus}\n')
print(f'{format_plus}\n')


#memformat persen
persentase = 0.73984758
format_persen = f'persen = {persentase:.2%}'  # 2 nya <--  untuk nampilan berapa angka di belakang koma
print(f'{format_persen}\n')

#melakukan operasi aritmatika di dalam placeholder {}
harga = 70000
jumlah = 9
format_jumlah = f'Rp. {harga*jumlah:,}'
print(format_jumlah)
print(f'{type(format_jumlah)}\n')

# format angka lain (binary, octal, hexadecimal)

nomer = 797

format_binary = f'binary from {nomer} = {bin(nomer)}'
format_octal = f'octal from {nomer} = {oct(nomer)}'
format_hex = f'hex from {nomer} = {hex(nomer)}'

print(format_binary)
print(format_octal)
print(format_hex)