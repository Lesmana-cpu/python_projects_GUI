#membuat area rentang dari angka
#+++++++3--------10+++++++++
userOptions = float(input('masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 :   '))
#++++3---------
kurangDari3 = userOptions < 3
#------10++++++
lebihDari10 = userOptions > 10

correct = kurangDari3 or lebihDari10
if correct == True:
    print(f"jawaban anda adalah {correct}")
    print("dan anda pintar")
else:
    print('lol')


print('\n', 20*'#', '\n')


#---------3+++++++++10---------
userOptions = float(input('masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari dari 10 :   '))
#------3++++++++++
lebihDari3 = userOptions > 3 
#++++++++10---------
kurangDari10 = userOptions < 10
correct2 = lebihDari3 and kurangDari10 
if correct2 == True:
    print(f'jawabam anda adalah = {correct2}')
    print('dan anda pintar')
else:
    print("tolol")




#-------0++++++++5--------8++++++++11-----
user1 = float(input('masukkan angka yang bernilai \nlebih dari 0 dan kurang dari 5 \natau \nlebih dari 8 dan kurang dari 11\n :   '))

lebihDari0 = user1 > 0 
kurangDari5 = user1 < 5
lebihDari8 = user1 > 8
kurangDari11 = user1 < 11

correct1 = lebihDari0 and kurangDari5
correct2 = lebihDari8 and kurangDari11
correct3 = correct1 or correct2
if correct3 == True:
    print(f"jawaban anda adalah = {correct3}")
    print('dan anda pintar')
else:
    print("anda tolol")



while True:
#+++++++0------5++++++8-----11+++++++

    user2 = float(input('masukkan angka yang bernilai \nkurang dari 0 atau lebih dari 5, atau kurang dari 8, atau lebih dari 11\n :   '))

    kurangDari0 = user2 < 0
    l5 = user2 > 5
    k8 = user2 < 8
    lebihDari11 = user2 > 11

    jwb1 = l5 and k8
    jwb2 = kurangDari0 or lebihDari11

    jwb3 = jwb1 or jwb2
    if jwb3 == True:
        print(f'jawaban anda adalah {jwb3}')
        print("dan anda adalah orang pintar")
    else:
        print("anda tolol")

    p = str(input("masukkan y/n"))
    if p == 'n':
        break
    else:
        print("again")



