
# #studi kasus

# def fungsi(parameter):
#     hasil = parameter ** 2
#     print(hasil)
    
# fungsi(1)
# fungsi("L7")
# fungsi(True)


# penggunaan type hints


def fungsi_with_hints(argument:bool):   # walaupun arument:bool, tapi badannya itu harus int, jadi type nya bakalan int
    output = 3**argument                     # (x) -> int, mengubah keluarannya si return yg tadi nya any menjadi int
    return output

hasil = fungsi_with_hints(9)
print(hasil)
print(f"{type(hasil)}\n")

def display(argument:str):
    print(argument)
    
display('asep')