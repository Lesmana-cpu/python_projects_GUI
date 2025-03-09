# operator dictionary

# list_nya = ['suki', 1, 7, 'ngaji']

data_dict = {
    'key': 'value',
    'L7' : 'Lesmana',
    'NT' : 'Nikola Tesla',
    'AE' : 'Albert Einstein',
    'KL' : 'Kali Linux',
#     'LS' : list_nya,
#        1 : 'Lesman',
#  'nilai' : 100,
#  'double_str' : 'halo ' 'hai'
}

# panjang dictionary
len_dict = len(data_dict)
print(f'panjang data_dict adalah = {len_dict}')


# cek key exist atau tidak
key = 'L7'
check_key = key in data_dict

if check_key == True:
    print(f'{key}, ada di data_dict: {data_dict}')
else:
    print(f'{key}, tidak ada di data_dict')
    
    
# mengakses value (read) dengan get, memakai kurung (), bukan []
print(data_dict.get('L7'))

    # print(data_dict('L9'))  <-- kalo key nya ga ada akan error
print(data_dict.get('L9')) # <-- jadi solusinya memakai get, untuk mengecek apakah 'L9' ada di data_dict
print(data_dict.get('L9', 'L9 tidak ada di dalam data_dict'))  # <-- , 'L9 tidak ada di dalam data_dict' : ini mengubah outpu yang tadinya None menjadi = L9 tidak ada di dalam data_dict 


# mengupdate data
data_dict['KL'] = 'kali'  # <-- mengubah isi (value) KL menjadi kali
print(data_dict)
data_dict['ATG'] = 'Alexander The Great' # <-- menambahkan data, 'ATG' = key, 'Alexander The Great' = value 
print(data_dict)

data_dict.update({'sk' : 'Suki'}) # <-- kalo datanya tidak ada bakalalan di add (di tambahkan)
print(data_dict)
data_dict.update({'KL' : 'Kali Linux'})
print(data_dict)


# mendelete data
del data_dict['KL']  # <-- menghapus key = KL & valuenya
print(data_dict)