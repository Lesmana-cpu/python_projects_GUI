# dictionary (dicti)  -> assocative array
# identifier -> key

data_list = ['asep', 'suki', 'KARL']

data_dict = {
    'key': 'value',            # <-- Key-value pair biasa
    'L7' : 'Lesmana',          # <-- contoh penggunaanya
    'NT' : 'Nikola Tesla',
    'AE' : 'Albert Einstein',
    'KL' : 'Kali Linux',
    'LS' : data_list,          # <-- LS adalah variabel yang berisi data_list
       1 : 'Lesman',           # <-- contoh key nya integer, value nya string
 'nilai' : 100,                # <-- contoh key nya string, value nya integer
 'double_str' : 'halo ' 'hai'  # <-- String yang ditulis terpisah
}

print(data_dict['L7'])
print(data_dict['KL'])
print(data_dict['double_str'])
print(data_dict[1])
print(data_dict['nilai'])
print(data_dict['LS'])

