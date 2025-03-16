# GUI

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo as si

# Init
window = tk.Tk()
window.configure(bg="black")  # <-- warna background
window.geometry("300x200")    # <-- ukuran
window.resizable(True,False)  # <-- ukurannya tidak bisa di perbesar untuk "y", "x" bisa
window.title("Katakan Hai ke Suki")

# Variable
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()
NAMA_TENGAH = tk.StringVar()

# frame input
input_frame = ttk.Frame(window)
# penempatan ada 3 = Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True )

# komponen-komponen
 # 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

 # 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable = NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama tengah
nama_tengah_label = ttk.Label(input_frame, text="Nama tengah (opsional):")
nama_tengah_label.pack(padx=10, fill="x", expand=True)

 # 4. entry nama tengah
nama_tengah_entry = ttk.Entry(input_frame, textvariable = NAMA_TENGAH)
nama_tengah_entry.pack(padx=10, fill="x", expand=True)

 # 5. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

 # 6. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable = NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

 # 7. tombol
def tombol_click():
    # print(f"hai {NAMA_DEPAN.get()} {NAMA_TENGAH.get()} {NAMA_BELAKANG.get()}")    # <-- ini outpunya ke terminal
    
    pesan = f"Hai!, {NAMA_DEPAN.get()} {NAMA_TENGAH.get()} {NAMA_BELAKANG.get()}, You so goodloking!!"
    si(title="for you", message=pesan)
 
sapa_button = ttk.Button(input_frame, text="Sapa", command=tombol_click)
sapa_button.pack(fill="x", expand=True, padx=10, pady=10)

# Main loop window
window.mainloop()