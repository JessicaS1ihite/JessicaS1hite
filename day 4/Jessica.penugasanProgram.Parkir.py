import tkinter as tk
from tkinter import ttk, messagebox

BIAYA_PER_JAM = 2000
data_parkir = []

def hitung_biaya():
    try:
        plat = entry_plat.get()
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())

        if keluar <= masuk:
            messagebox.showerror("Error", "Waktu keluar harus lebih besar!")
            return

        lama = keluar - masuk
        biaya = lama * BIAYA_PER_JAM
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, biaya)

        data = (plat, masuk, keluar, biaya)
        data_parkir.append(data)

        update_tabel()
        entry_plat.delete(0, tk.END)
        entry_masuk.delete(0, tk.END)
        entry_keluar.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Masukkan data dengan benar!")

def update_tabel():
    for i in tree_keluar.get_children():
        tree_keluar.delete(i)
    for i in tree_bayar.get_children():
        tree_bayar.delete(i)

    # Urut terakhir keluar
    for d in reversed(data_parkir):
        tree_keluar.insert("", tk.END, values=d)

    # Urut bayar terbanyak
    for d in sorted(data_parkir, key=lambda x: x[3], reverse=True):
        tree_bayar.insert("", tk.END, values=d)

# Window
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("900x450")

# ===== INPUT =====
frame_input = tk.Frame(root)
frame_input.pack(side=tk.LEFT, padx=20)

tk.Label(frame_input, text="No Plat Polisi").grid(row=0, column=0, sticky="w")
entry_plat = tk.Entry(frame_input)
entry_plat.grid(row=0, column=1)

tk.Label(frame_input, text="Waktu Masuk").grid(row=1, column=0, sticky="w")
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=1, column=1)

tk.Label(frame_input, text="Waktu Keluar").grid(row=2, column=0, sticky="w")
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=2, column=1)

tk.Label(frame_input, text="Biaya").grid(row=3, column=0, sticky="w")
entry_biaya = tk.Entry(frame_input)
entry_biaya.grid(row=3, column=1)

tk.Button(frame_input, text="Hitung", command=hitung_biaya).grid(row=4, column=1, pady=10)

# ===== BIAYA PER JAM =====
tk.Label(
    root,
    text="Biaya Per Jam\nRp. 2.000",
    fg="red",
    font=("Arial", 16, "bold")
).pack(pady=20)

# ===== TABEL =====
frame_table = tk.Frame(root)
frame_table.pack(side=tk.BOTTOM, pady=10)

kolom = ("No Plat", "Masuk", "Keluar", "Biaya")

tk.Label(frame_table, text="List Pelanggan Urut Terakhir Keluar").grid(row=0, column=0)
tree_keluar = ttk.Treeview(frame_table, columns=kolom, show="headings")
for k in kolom:
    tree_keluar.heading(k, text=k)
tree_keluar.grid(row=1, column=0, padx=10)

tk.Label(frame_table, text="List Pelanggan Banyak Bayar").grid(row=0, column=1)
tree_bayar = ttk.Treeview(frame_table, columns=kolom, show="headings")
for k in kolom:
    tree_bayar.heading(k, text=k)
tree_bayar.grid(row=1, column=1, padx=10)

root.mainloop()