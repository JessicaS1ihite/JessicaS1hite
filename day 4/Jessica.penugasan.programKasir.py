import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        qty = int(entry_qty.get())
        total = harga * qty
        label_total.config(text=f"Total: Rp {total:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Window utama
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x250")

# Label & Entry Harga
tk.Label(root, text="Harga:").pack(pady=5)
entry_harga = tk.Entry(root)
entry_harga.pack()

# Label & Entry Kuantitas
tk.Label(root, text="Kuantitas:").pack(pady=5)
entry_qty = tk.Entry(root)
entry_qty.pack()

# Tombol Hitung
tk.Button(root, text="Hitung Total", command=hitung_total).pack(pady=15)

# Label Total
label_total = tk.Label(root, text="Total: Rp 0.00", font=("Arial", 11, "bold"))
label_total.pack()

root.mainloop() 