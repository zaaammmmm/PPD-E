# Mengimpor library tkinter
import tkinter as tk
from tkinter import messagebox

# Membuat jendela utama
window = tk.Tk()

# Memberikan judul pada jendela
window.title("Form Biodata Mahasiswa")

# Mengatur ukuran jendela (lebar x tinggi)
window.geometry("500x600")
window.configure(bg="white")

# Menambahkan label judul
title_label = tk.Label(window, text="Form Biodata Mahasiswa", font=("Arial", 16))
title_label.pack(pady=10)

# Membuat frame utama
main_frame = tk.Frame(master=window, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(1, weight=1)

# # Membuat label data
# label_data = tk.Label(
#     master=window,
#     text="Masukkan Data Mahasiswa",
#     font=("Arial", 16, "bold")
# )

# # Menampilkan label dengan pack
# label_data.pack(pady=20)

# Variabel untuk radiobutton jenis kelamin
var_jk = tk.StringVar(value="Pria")

# Label jenis kelamin
label_jk = tk.Label(master=main_frame, text="Jenis Kelamin:", font=("Arial", 12))
label_jk.grid(row=4, column=0, sticky="W", pady=5)

# Frame untuk radiobutton
frame_jk = tk.Frame(master=main_frame)
frame_jk.grid(row=4, column=1, sticky="W")

# Radiobutton pria dan wanita
radio_pria = tk.Radiobutton(master=frame_jk, text="Pria", variable=var_jk, value="Pria")
radio_pria.pack(side=tk.LEFT)

radio_wanita = tk.Radiobutton(master=frame_jk, text="Wanita", variable=var_jk, value="Wanita")
radio_wanita.pack(side=tk.LEFT)

# Menjalankan event loop
window.mainloop()
