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

# Variabel untuk checkbox
var_setuju = tk.IntVar()

# Checkbox persetujuan
check_setuju = tk.Checkbutton(
    master=main_frame,
    text="Saya menyetujui pengumpulan data ini.",
    variable=var_setuju,
    font=("Arial", 10)
)
check_setuju.grid(row=5, column=0, columnspan=2, pady=10, sticky="W")

# Menjalankan event loop
window.mainloop()
