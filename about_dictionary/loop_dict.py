# looping dictionary

teman_teman = {
    'pan' : 'repan',
    'pa' : 'dapa',
    'suk' : 'suki liar',
    'sep' : 'asep',
    'jon' : 'joni'
}

# looping first try (yang keluar adalah key nya)
print('ini hasil looping teman-temannya aja:')

for index, teman in enumerate (teman_teman, start= 1):
    print(f'{index}.{teman}\t<-- hasilnya key nya doang')
print('\n\n')   


# operator/method untuk mengambil item / iterables
# key
print('ini ngeprint key nya aja:')
keys = teman_teman.keys()
print(keys)
print('\n')

print('ini looping key nya aja:')

for index, key in enumerate(teman_teman.keys(), start = 1) :
    print(f'key ke {index} adalah = {key}')
print('\n\n')


# value
print('ini ngeprint value nya aja:')
values = teman_teman.values()
print(values)
print('\n')

print('ini looping value nya aja:')

for index, value in enumerate (teman_teman.values(), start= 1):
    print(f'value ke {index} adalah = {value}')
print('\n\n')


# items
print('ini ngeprint item / pasangan (key & value)')
items = teman_teman.items()
print(items)
print('\n')

print('ini looping item / pasangan (key & value)')

for index, item in enumerate (teman_teman.items(), start= 1):
    print(f'{index}.{item}')
print('\n\n')


# gabungan ketiganya
print('ini looping gabungan ketiganya')    

for index, (key, value) in enumerate (teman_teman.items(), start= 1):
    print(f'{index}.key = {key} value = {value}')