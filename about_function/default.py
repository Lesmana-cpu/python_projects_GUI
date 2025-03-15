'''default argument'''
# def fungsi(argument = nilai defaulnya):


# example 1
from encodings.punycode import T


def say_hello(nama = 'none'):
    if nama == 'none':
        print('masukkan value nya LOL? ')
    else:
        print(f'hai {nama}')
        
say_hello('L7')
say_hello()



# example 2
def sapa( nama = 'suki', pesan = 'kamu lol'):
    print(f"hai {nama}, {pesan}")

sapa('KARL', 'udah kaya?')
sapa()


# example 3
def hitung_pangkat(angka, pangkat=2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(5))

change = hitung_pangkat(pangkat=3, angka=7)
print(change)


# example 4
def string(nama= False):
    hasil = f'hai {nama}'  # <-- merubah jadi str
    return hasil
print(type(string(9)))


# example 5
def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(7, input4=5))
