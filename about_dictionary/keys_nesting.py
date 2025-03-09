import datetime as dt


mahasiswa_1 = {
    'nama':'asep',
    'nim'  : '10000',
    'sks_lulus' : 130,
    'beasiswa' : True,
    'lahir':dt.datetime(1999,7,27)    
}


mahasiswa_2 = {
    'nama':'joko',
    'nim'  : '10000',
    'sks_lulus' : 110,
    'beasiswa' : True,
    'lahir':dt.datetime(1989,8,3)    
}



mahasiswa_3 = {
    'nama':'suki',
    'nim'  : '19700',
    'sks_lulus' : 124,
    'beasiswa' : False,
    'lahir':dt.datetime(2001,7,27)    
}


data_mahasiswa =  {
    'MAH001' : mahasiswa_1,
    'MAH002' : mahasiswa_2,
    'MAH003' : mahasiswa_3
}



print('\nlooping ke-1:')
while True:
    print('='*75)
    mahasiswa = {}
    mahasiswa['nama'] = input('Nama Mahasiswa : ')
    mahasiswa['nim'] = input('NIM Mahasiswa : ')
    mahasiswa['sks_lulus'] = int(input('SKS Lulus : '))
    TANGGAL_LAHIR = int(input('Tanggal lahir (1-31) : '))
    BULAN_LAHIR = int(input('Bulan lahir (1-12) : '))
    TAHUN_LAHIR = int(input('Tahun lahir (YYYY) : '))
    
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    beasiswa = input('Apakah mahasiswa mendapat beasiswa? (y/n) : ').strip().lower()  
    mahasiswa['beasiswa'] = True if beasiswa == 'y' else False

    id_baru = f"MAH{str(len(data_mahasiswa) + 1).zfill(3)}"
    data_mahasiswa[id_baru] = mahasiswa  # Perbaikan: Simpan data dengan ID baru

    print(f'{"NO":<4}{"KEY":>7} {"Nama":>8} {"SKS":>5} {"Beasiswa":>10} {"Lahir":>8}')
    print('='*51)
    
    for index, (KEY, mahasiswa) in enumerate(data_mahasiswa.items(), start=1):
        NAMA = mahasiswa['nama']      #ini contoh harus mengambil datanya lagi
        NIM = mahasiswa['nim']
        SKS = mahasiswa['sks_lulus']
        BEASISWA = mahasiswa['beasiswa']
        LAHIR = mahasiswa['lahir'].strftime('%x')
        
        print(f'{index} {".":<3} {KEY:<6} {NAMA:>6} {SKS:>5} {BEASISWA:>7} {LAHIR:>13}')
    
    pilihan = str(input('apakah kamu ingin menambahkan data baru lagi? y/n\n'))
    
    if pilihan == 'n':
        break
    else:
        continue 
    
    



print('\n\n\nlooping ke-2:')       # langsung mengambil key dan data mahasiswa sekaligus, jadi lebih cepat dan efisien

print(f'{'NO':<4}{'KEY':>7} {'Nama':>8} {'SKS':>5} {'Beasiswa':>10} {'Lahir':>8}')
print('='*51)

for index, (key, mahasiswa) in enumerate (data_mahasiswa.items(), start=1):
    print(f'{index} {".":<3}  {key:<6} {mahasiswa["nama"]:>6} {mahasiswa["sks_lulus"]:>5} {mahasiswa["beasiswa"]:>7} {mahasiswa["lahir"].strftime("%x"):>13}')
     