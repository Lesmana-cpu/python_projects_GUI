# copy dictionary

data_dict = {
    'key': 'value',
    'L7' : 'Lesmana',
    'NT' : 'Nikola Tesla',
    'AE' : 'Albert Einstein',
    'KL' : 'Kali Linux'
}


friends = data_dict
friendsip = data_dict.copy()


data_dict['L7'] = 'man man'
print(f'{data_dict}\n')
print(f'{friends}\n')
print(f'{friendsip}\n')


print(f'data yang asli lokasi memory nya di -> {hex(id(data_dict))}')
print(f'data yang di copy dengan ("data_asli = data_baru") lokasi memory nya di -> {hex(id(friends))}')
print(f'data yang copy menggunakan ("data_asli = data_baru.copy()") lokasi memory nya di -> {hex(id(friendsip))}\n')


# pop dictionary (mengambil berdasarkan key)
data_L7 = friends.pop('L7')    # <-- ambil key nya
print(f'data_L7 = {data_L7}')
print(f'jadi data friends :\n{friends}\n')


# popitem mengambil yang terakhir
data_terakhir = friends.popitem()
print(f'data terakhir = {data_terakhir}')
print(f'jadi data friends sekarang adalah = {friends}')