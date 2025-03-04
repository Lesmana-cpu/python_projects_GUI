# Operasi Bitwise dalam Python

# OR (|)
print('########## OR ##########')
a = 5
b = 7
c = a | b
print(f'nilai {a} binary {format(a, "08b")}')
print(f'nilai {b} binary {format(b, "08b")}')
print(f'{format(a, "08b")} | {format(b, "08b")} = {format(c, "08b")} atau {c}')

# AND (&)
print('\n########## AND ##########')
d = 7
e = 9
f = d & e
print(f'nilai {d} binary {format(d, "08b")}')
print(f'nilai {e} binary {format(e, "08b")}')
print(f'{format(d, "08b")} & {format(e, "08b")} = {format(f, "08b")} atau {f}')

# XOR (^)
print('\n########## XOR ##########')
a = 7
b = 9
c = a ^ b
print(f'nilai {a} binary {format(a, "08b")}')
print(f'nilai {b} binary {format(b, "08b")}')
print(f'{format(a, "08b")} ^ {format(b, "08b")} = {format(c, "08b")} atau {c}')

# NOT (~)
print('\n########## NOT ##########')
b = 9
c = ~b
print(f'nilai {b} binary {format(b, "08b")}')
print(f'NOT {format(b, "08b")} = {format(c & 0xFF, "08b")} atau {c} (dalam two\'s complement)')

# SHIFT RIGHT (>>)
print('\n########## SHIFT RIGHT ##########')
y = 7
shift_right = 2
z = y >> shift_right
print(f'nilai {y} binary {format(y, "08b")}')
print(f'{format(y, "08b")} >> {shift_right} = {format(z, "08b")} atau {z}')

# SHIFT LEFT (<<)
print('\n########## SHIFT LEFT ##########')
y = 7
shift_left = 2
z = y << shift_left
print(f'nilai {y} binary {format(y, "08b")}')
print(f'{format(y, "08b")} << {shift_left} = {format(z, "08b")} atau {z}')

