# Mengimpor library tkinter
import tkinter as tk
from tkinter import messagebox

# Membuat jendela utama
window = tk.Tk()

# Memberikan judul pada jendela
window.title("Form Biodata Mahasiswa")

# Mengatur ukuran jendela (lebar x tinggi)
window.geometry("500x600")
window.configure(bg="beige")

# Menambahkan label judul
title_label = tk.Label(window, text="Form Biodata Mahasiswa", font=("Arial", 16))
title_label.pack(pady=10)

# # Membuat label data
# label_data = tk.Label(
#     master=window,
#     text="Masukkan Data Mahasiswa",
#     font=("Arial", 16, "bold")
# )

# # Menampilkan label dengan pack
# label_data.pack(pady=20)

# Label untuk input nama
label_nama = tk.Label(master=window, text="Nama Lengkap:", font=("Arial", 12))
label_nama.pack(pady=5)

# Entry untuk input nama
entry_nama = tk.Entry(master=window, width=50)
entry_nama.pack(pady=5)

# Input NIM
label_nim = tk.Label(master=window, text="NIM:", font=("Arial", 12))
label_nim.pack(pady=5)
entry_nim = tk.Entry(master=window, width=50)
entry_nim.pack(pady=5)

# Input Jurusan
label_jurusan = tk.Label(master=window, text="Jurusan:", font=("Arial", 12))
label_jurusan.pack(pady=5)
entry_jurusan = tk.Entry(master=window, width=50)
entry_jurusan.pack(pady=5)

# Fungsi untuk menampilkan input
def tampilkan_data():
    nama = entry_nama.get()
    nim = entry_nim.get()
    jurusan = entry_jurusan.get()

    # Tampilkan di MessageBox
    messagebox.showinfo("Biodata Mahasiswa", f"Nama: {nama}\nNIM: {nim}\nJurusan: {jurusan}")

# Tombol Submit
btn_submit = tk.Button(window, text="Simpan", font=("Arial", 12), command=tampilkan_data)
btn_submit.pack(pady=20)

# Menjalankan event loop
window.mainloop()
