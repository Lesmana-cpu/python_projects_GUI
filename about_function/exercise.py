#                                         ''' LATIHANN '''

def header():
    print(f"{'MENGHITUNG LUAS & KELILING PERSEGI PANJANG':^50}")
    print(f"{'-'*45:^50}")
    
def input_user():
    panjang = int(input("masukkan panjangnya: "))
    lebar = int(input("masukkan lebarnya: "))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    return panjang*lebar

def hitung_keliling(panjang, lebar):
    return 2*(panjang*lebar)
    
def display(message, value):
    print(f'hasil perhitungan {message} = {value}')



while True:
    header()
    panjang, lebar = input_user()
    LUAS = hitung_luas(panjang, lebar)
    KELILING = hitung_keliling(panjang, lebar)
    
    pilihan = int(input('kamu ingin memilih penjumlahan yang mana\n1.luas\n2.keliling\n: '))
    if pilihan == 1:
        display("luas", LUAS) 
    elif pilihan == 2:
        display('keliling', KELILING)
    else:
        print('hanya boleh memilih yang ada di menu!')
        continue
    
    pilihan2 = str(input('apakah kamu ingin melanjutkannya kembali?  y/n\n: '))
    if pilihan == 'n':
        break

print('terimakasih telah memakai program saya')