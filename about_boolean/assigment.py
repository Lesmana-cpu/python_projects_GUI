a = 10 #ini assigment
print(f'\nnilai a = {a}')
 
a += 1    #ini a=a + 1
print(f'nilai a += 1 itu hasilnya = {a}')

a = 10
a -= 2
print(f'nilai a -= 2 itu hasilnya = {a}\n')

a = 10
a *= 3
print(f'nilai a *= 3 itu hasilnya = {a}')

a = 10
a /= 3
print(f'nilai a /= 3 itu hasilnya = {a}')

a = 10
a %= 3
print(f'nilai a %= 3 itu hasilnya = {a}')

a = 10
a //= 3
print(f'nilai a //= 3 itu hasilnya = {a}')

a = 10
a **= 2
print(f'nilai a **= 2 itu hasilnya = {a}\n')


#ini |
c = True
print(f'c = {c}')
c |= True
print(f'nilai c |= True, hasilnya = {c}')

c = True
c |= False
print(f'nilai c |= False, hasilnya = {c}\n')

#kebalikann

c = False
print(f'c = {c}')
c |= False
print(f'nilai c |= False, hasilnya = {c}')

c = False
c |= True
print(f'nilai c |= True, hasilnya = {c}\n')


#ini &
d = True
print(f'd = {d}')
d &= True
print(f'nilai d &= True, hasilnya = {d}')

d = True
d &= False
print(f'nilai d &= False, hasilnya {d}\n')

#kebalikan

d = False
print(f'd = {d}')
d &= False
print(f'nilai d &= False, hasilnya = {d}')

d = False
d &= True
print(f'nilai d &= True, hasilnya {d}\n')

#ini XOR

e = True
print(f'e = {e}')
e ^= True
print(f'nilai e ^= True, hasilnya {e}')

e = True
e ^= False
print(f'nilai e ^= False, hasilnya {e}\n')

#kebalikan
e = False
print(f'e = {e}')
e ^= False
print(f'nilai e ^= False, hasilnya {e}')

e = False
e ^= True
print(f'nilai e ^= True, hasilnya {e}\n')


f = 0b0100
print(f'\n nilai f = {format(f, '04b')} bit, atau {f}')
f >>= 2
print(f'\n nilai f >>= 2, hasilnya {format(f, '04b')} bit, atau {f}\n')

g = 0b00001000
print(f'\n nilai g = {format(g, '04b')} bit, atau {g}')
g <<= 3
print(f'\n nilai g <<= 3, hasilnya {format(g, '04b')} bit, atau {g}')