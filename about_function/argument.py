def hello_world(name):
    print(f'hallo {name}')

    
hello_world('lesmana')



# say hay

def say_hay(list_suki):
    data_suki = list_suki.copy()  # <-- kalo ga make copy maka saat data yang ada di dalam fungsi di rubah, maka data aslinya juga ikut berubah
    for suki in data_suki:
        print(f'hai {suki}')


daftar_suki = ['asep', 'jamal', 'kokoci', 'ujang', 'dadang'] 
say_hay(daftar_suki)

    
    