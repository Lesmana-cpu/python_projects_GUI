import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror as se

def calculate():
    num1 = float(angka_num1.get())
    num2 = float(angka_num2.get())
    operation = angka_operation.get()
    
    if num2 == 0 and operation in [":", "%", "//"]:
        se("Error", "Tidak bisa membagi dengan nol")
        return
    
    if operation == "+":
        hasil = num1 + num2
    elif operation == "-":
        hasil = num1 - num2
    elif operation == "x":
        hasil = num1 * num2
    elif operation == ":":
        hasil = num1 / num2
    elif operation == "%":
        hasil = num1 % num2
    elif operation == "//":
        hasil = num1 // num2
    else:
        se("Error", "Operasi tidak valid")
        return
 # Menampilkan hasil sebagai bilangan bulat jika genap
    hasil_nya = int(hasil) if hasil % 2 == 0 else float(hasil)
    result.config(text=f"Hasil: {hasil_nya}")

# Window setup
window = tk.Tk()
window.configure(bg="white")
window.geometry("350x300")
window.resizable(False, True)
window.title("Kalkulator")

# Frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Widgets
angka_list = [str(i) for i in range(101)]

num1 = ttk.Label(input_frame, text="Angka 1:")
num1.pack(padx=10, fill="x")
angka_num1 = ttk.Combobox(input_frame, values=angka_list)
angka_num1.pack(padx=10, fill="x")
angka_num1.current(0)

num2 = ttk.Label(input_frame, text="Angka 2:")
num2.pack(padx=10, fill="x")
angka_num2 = ttk.Combobox(input_frame, values=angka_list)
angka_num2.pack(padx=10, fill="x")
angka_num2.current(0)

op = ttk.Label(input_frame, text="Operasi:")
op.pack(padx=10, fill="x")
angka_operation = ttk.Combobox(input_frame, values=["+", "-", "x", ":", "%", "//"])
angka_operation.pack(padx=10, fill="x")
angka_operation.current(0)

btn_calculate = ttk.Button(input_frame, text="Hitung", command=calculate)
btn_calculate.pack(fill="x", expand=True, padx=10, pady=10)

result = ttk.Label(input_frame, text="Hasil: ")
result.pack(padx=10, fill="x")

window.mainloop()
