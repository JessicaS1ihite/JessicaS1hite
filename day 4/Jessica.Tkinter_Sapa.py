import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init window
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa")

# Variable
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Fungsi
def tombol_click():
    pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Have nice day"
    showinfo(title="Hi", message=pesan)

# Frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Label & Entry Nama Depan
ttk.Label(input_frame, text="Nama Depan:").pack(fill="x", expand=True)
ttk.Entry(input_frame, textvariable=NAMA_DEPAN).pack(padx=10, fill="x", expand=True)

# Label & Entry Nama Belakang
ttk.Label(input_frame, text="Nama Belakang:").pack(fill="x", expand=True)
ttk.Entry(input_frame, textvariable=NAMA_BELAKANG).pack(padx=10, fill="x", expand=True)

# Tombol
ttk.Button(input_frame, text="Sapa", command=tombol_click)\
    .pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()