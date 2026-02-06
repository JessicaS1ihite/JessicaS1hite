import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = {
        "Nama": entry_nama.get(),
        "Tanggal Lahir": entry_tgl.get(),
        "Asal Sekolah": entry_asal.get(),
        "NISN": entry_nisn.get(),
        "Nama Ayah": entry_ayah.get(),
        "Nama Ibu": entry_ibu.get(),
        "No HP": entry_hp.get(),
        "Alamat": text_alamat.get("1.0", tk.END)
    }

    messagebox.showinfo(
        "Data Tersimpan",
        "Data siswa berhasil disimpan!"
    )
    print(data)  # untuk bukti output di console

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_asal.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# Window
root = tk.Tk()
root.title("MainWindow")
root.geometry("600x700")
root.configure(bg="#e6e6e6")

# ===== JUDUL =====
judul = tk.Label(
    root,
    text="DATA SISWA BARU",
    bg="#a8edf0",
    font=("Arial", 16, "bold"),
    pady=15
)
judul.pack(fill=tk.X)

frame = tk.Frame(root, bg="#e6e6e6")
frame.pack(padx=20, pady=10, fill=tk.BOTH)

def buat_label(text, row):
    tk.Label(frame, text=text, bg="#e6e6e6").grid(row=row, column=0, sticky="w")

def buat_entry(row):
    e = tk.Entry(frame, width=50)
    e.grid(row=row, column=1, pady=5)
    return e

buat_label("Nama Lengkap", 0)
entry_nama = buat_entry(0)

buat_label("Tanggal Lahir", 1)
entry_tgl = buat_entry(1)

buat_label("Asal Sekolah", 2)
entry_asal = buat_entry(2)

buat_label("NISN", 3)
entry_nisn = buat_entry(3)

buat_label("Nama Ayah", 4)
entry_ayah = buat_entry(4)

buat_label("Nama Ibu", 5)
entry_ibu = buat_entry(5)

buat_label("Nomor Telepon / HP", 6)
entry_hp = buat_entry(6)

buat_label("Alamat", 7)
text_alamat = tk.Text(frame, width=38, height=5)
text_alamat.grid(row=7, column=1, pady=5)

# ===== TOMBOL =====
frame_btn = tk.Frame(root, bg="#7fcfd1", pady=15)
frame_btn.pack(fill=tk.X)

tk.Button(
    frame_btn, text="Hapus", bg="#c96b3c", fg="white",
    width=10, command=hapus_data
).pack(side=tk.LEFT, padx=150)

tk.Button(
    frame_btn, text="Simpan", bg="#c96b3c", fg="white",
    width=10, command=simpan_data
).pack(side=tk.RIGHT, padx=150)

root.mainloop()