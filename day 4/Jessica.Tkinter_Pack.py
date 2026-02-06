import tkinter as tk

# Membuat window utama
root = tk.Tk()
root.title("Contoh Pack Layout")

# Membuat label
label = tk.Label(root, text="Label 1")
label.pack()

# Membuat tombol
button = tk.Button(root, text="Tombol 1")
button.pack()

# Membuat checkbox
checkbox = tk.Checkbutton(root, text="Centang 1")
checkbox.pack()

# Menjalankan aplikasi
root.mainloop()