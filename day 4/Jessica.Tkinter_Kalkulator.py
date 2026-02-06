import tkinter as tk
from tkinter import ttk

def hitung():
    try:
        angka1 = float(angka1_entry.get())
        angka2 = float(angka2_entry.get())
        operator = operator_combobox.get()

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        elif operator == "/":
            if angka2 == 0:
                hasil = "Tidak bisa dibagi 0"
            else:
                hasil = angka1 / angka2
        else:
            hasil = "Pilih operator!"

    except ValueError:
        hasil = "Masukkan angka yang valid!"

    hasil_label.config(text=str(hasil))

# Window
window = tk.Tk()
window.title("Kalkulator")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

# Angka 1
ttk.Label(input_frame, text="Angka 1:").grid(row=0, column=0, sticky="w")
angka1_entry = ttk.Entry(input_frame)
angka1_entry.grid(row=0, column=1)

# Angka 2
ttk.Label(input_frame, text="Angka 2:").grid(row=1, column=0, sticky="w")
angka2_entry = ttk.Entry(input_frame)
angka2_entry.grid(row=1, column=1)

# Operator
ttk.Label(input_frame, text="Operator:").grid(row=2, column=0, sticky="w")
operator_combobox = ttk.Combobox(
    input_frame,
    values=["+", "-", "*", "/"],
    state="readonly"
)
operator_combobox.grid(row=2, column=1)
operator_combobox.current(0)

# Tombol
ttk.Button(window, text="Hitung", command=hitung).pack(pady=10)

# Hasil
hasil_label = ttk.Label(window, text="")
hasil_label.pack()

window.mainloop()