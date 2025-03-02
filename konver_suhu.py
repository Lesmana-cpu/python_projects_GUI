def perbandingan_suhu():



    while True:
            pilihan = str(input("kamu ingin konversi dari suhu apa?...\n-celcius \n-reamur \n-fahrenheit \n-kelvin \nmasukkan jawabanmu\njawaban = "))
            
            if pilihan == "celcius":
                    perubahan_c = int(input("kamu mau ubah suhu celcius ke suhu apa?... \n1.reamur \n2.fahrenheit \n3.kelvin \nsilahkan di pilih mau nomor berapa \U0001F604 \n"))
                    
                    celcius = float(input("masukkan suhu dalam celcius....\n"))
                    reamur_c = (4/5) * celcius
                    fahrenheit_c = (9/5) * celcius + 32
                    kelvin_c = celcius + 273.15
                    print(f"suhu celciusnya = {celcius} °C")
                    if perubahan_c == 1:
                        print(f"sedangkan suhu reamurnya adalah = {reamur_c} °Re")
                    elif perubahan_c == 2:
                        print(f'sedangkan suhu fahrenheitnya adalah = {fahrenheit_c} °F')
                    elif perubahan_c == 3:
                        print(f'sedangkan suhu kelvinnya adalah = {kelvin_c} K')


            elif pilihan == "reamur":
                    perubahan_r = int(input("kamu mau ubah suhu reamur ke suhu apa?... \n1.celcius \n2.fahrenheit \n3.kelvin \nsilahkan di pilih mau nomor berapa \U0001F604 \n"))
                    reamur = float(input("masukkan suhu dalam reamur....\n"))
                    
                    celcius_r = 5/4 * reamur
                    fahrenheit_r = (9/4) * reamur + 32 
                    kelvin_r = (5/4) * reamur + 273.15
                    print(f"suhu reamur {reamur} °Re")
                    if perubahan_r == 1:
                        print(f'sedangkan suhu celciusnya adalah = {celcius_r} °C')
                    elif perubahan_r == 2:
                        print(f'sedangkan suhu fahrenheitnya adalah = {fahrenheit_r} °F')
                    elif perubahan_r == 3:
                        print(f'sedangkan suhu kelvinnya adalah = {kelvin_r} K')
                    

            elif pilihan == "fahrenheit":
                    perubahan_f = int(input("kamu mau ubah suhu fahrenheit ke suhu apa?... \n1.celcius \n2.reamur \n3.kelvin \nsilahkan di pilih mau nomor berapa \U0001F604 \n"))
                    fahrenheit = float(input("masukkan suhu dalam fahrenheit\n"))
                    
                    celcius_f = 5/9 * (fahrenheit - 32)
                    reamur_f = 4/9 * (fahrenheit - 32)
                    kelvin_f = (5/9 * (fahrenheit - 32)) + 273.15
                    print(f"suhu fahrenheit {fahrenheit} °F")
                    if perubahan_f == 1:
                        print(f'sedangkan suhu celciusnya adalah = {celcius_f} °C')
                    elif perubahan_f == 2:
                        print(f'sedangkan suhu reamurnya adalah = {reamur_f} °Re')
                    elif perubahan_f == 3:
                        print(f'sedangkan suhu kelvinnya adalah = {kelvin_f} K')
            
            
            elif pilihan == "kelvin":
                    perubahan_k = int(input("kamu mau ubah suhu kelvin ke suhu apa?... \n1.celcius \n2.reamur \n3.fahrenheit \nsilahkan di pilih mau nomor berapa \U0001F604 \n"))
                    kelvin = float(input("masukkan suhu dalam kelvin\n"))
                    
                    celcius_k = kelvin - 273.15
                    reamur_k = 4/5 * (kelvin - 273.15)
                    fahrenheit_k = ((kelvin - 273.15) * 9/5) + 32
                    print(f"suhu kelvin {kelvin} K")
                    if perubahan_k == 1:
                        print(f'sedangkan suhu celciusnya adalah = {celcius_k} °C')
                    elif perubahan_k == 2:
                        print(f'sedangkan suhu reamurnya adalah = {reamur_k} °Re')
                    elif perubahan_k == 3:
                        print(f'sedangkan suhu fahrenheitnya adalah = {fahrenheit_k} °F')
                    
            else :
                print("pilih yang ada aja!!")
            
            perulangan = str(input("\nApakah kamu ingin mengulang perbandingan suhunya? (y/n) \n")).lower()
            if perulangan == "n":
                print("\nTerima kasih telah menggunakan program ini!")
                break
            else:
                print("oke mulai ulang!!\n")

if __name__ == '__main__':
    perbandingan_suhu()