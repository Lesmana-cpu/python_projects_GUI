#width and multiline

# string multiline <-- dengan menggunakan new line ('\n')
nama = 'Lesmana'
umur = 16
plant = 'AI Development'

gabungan = f'nama = {nama} \nusia = {umur} \ncita-cita = {plant}\n'
data_str = '\n'+5*'='+'DATA STRING'+5*'='
print(data_str)
print(gabungan)


# string multi line

string = f'''nama = {nama}
umur = {umur}
cita-cita = {plant}
'''

print(data_str)
print(string)


#mengatur lebar
data = data_str             # :>7 <-- rata kanan dengan 7 karakter
                            # :<7 <-- rata kiri dengan 7 karakter
string_u = f'''             
nama      = {nama:>14}    
umur      = {umur:>14}
cita-cita = {plant:<7}
'''

print(data)
print(string_u)

