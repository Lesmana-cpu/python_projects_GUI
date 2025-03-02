#1. ini tanda ini \ bisa membuat " atau ' menjadi string


print('jum\'at')

#2. \\ backslash (\)
print('C:\\user\\mewing')

#3. tab
print('ayo\tsolat')

#4. backspace
print('ayo \bngaji')

#5. newline
print('o\nu')   #LF -> line feed -> unix, macos, linux
print('k-2')
print('o\ru')   #CR -> carriage return -> commodore, acorn, lisp
print('k-3')
print('o\r\nu') #CRLF -> line feed carriage return -> windows

#6. string literal atau raw (r)

    #salah
print('C:\new\folder')

    #benar
print(r'C:\new\folder')

#7. multiline literal string
print('''
nama : asep
kelas : 9
      
      ''')

# multiline literal string dan RAW
print(r'''
apala
www.lesman.\linux\new\folder
      
      ''')



a = 'haKJni'
b = a.upper()
print(b)
c = a.lower()
print(c)

