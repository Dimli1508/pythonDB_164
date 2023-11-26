import tkinter as tk
from tkinter import ttk
import sqlite3

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Membuat tabel nilai_siswa jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY,
        nama_siswa TEXT,
        biologi INTEGER,
        kimia INTEGER,
        matematika INTEGER,
        indonesia INTEGER,
        kewarganegaraan INTEGER,
        kesenian INTEGER,
        sejarah INTEGER,
        pai INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')
conn.commit()

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai
def prediksi_fakultas(biologi, kimia, matematika, indonesia, kewarganegaraan, kesenian, sejarah, pai, fisika, inggris):
    nilai = {'Kedokteran': biologi + kimia, 'Teknik': fisika + matematika, 'Bahasa': inggris + indonesia,
             'Agama': pai, 'Desain/DKV': kesenian, 'Hukum': kewarganegaraan + indonesia}

    # Menemukan fakultas dengan nilai tertinggi
    max_fakultas = max(nilai, key=nilai.get)
    return max_fakultas

# Fungsi untuk menangani tombol submit
def submit_nilai():
    nama_siswa = entry_nama.get()

    # membuat slider untuk nilai
    biologi = slider_biologi.get()
    kimia = slider_kimia.get()
    matematika = slider_matematika.get()
    indonesia = slider_indonesia.get()
    kewarganegaraan = slider_kewarganegaraan.get()
    kesenian = slider_kesenian.get()
    sejarah = slider_sejarah.get()
    pai = slider_pai.get()
    fisika = slider_fisika.get()
    inggris = slider_inggris.get()

    prediksi = prediksi_fakultas(biologi, kimia, matematika, indonesia, kewarganegaraan, kesenian, sejarah, pai, fisika, inggris)

    # Update label prediksi
    label_prediksi.config(text=f'Hasil Prediksi: {prediksi}')

    # mentimpan data ke database
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, kimia, matematika, indonesia, kewarganegaraan, kesenian, sejarah, pai, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama_siswa, biologi, kimia, matematika, indonesia, kewarganegaraan, kesenian, sejarah, pai, fisika, inggris, prediksi))

    conn.commit()
    print("Data berhasil disimpan!")

# Membuat GUI dengan tkinter
root = tk.Tk()
root.title("Prediksi Fakultas")

# Membuat label dan entry untuk nama siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

# Membuat slider dan label untuk nilai biologi
label_biologi = tk.Label(root, text="Biologi:")
label_biologi.grid(row=1, column=0)
slider_biologi = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_biologi.grid(row=1, column=1)

# Membuat slider dan label untuk nilai kimia
label_kimia = tk.Label(root, text="Kimia:")
label_kimia.grid(row=2, column=0)
slider_kimia = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_kimia.grid(row=2, column=1)

# Membuat slider dan label untuk nilai matematika
label_matematika = tk.Label(root, text="Matematika:")
label_matematika.grid(row=3, column=0)
slider_matematika = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_matematika.grid(row=3, column=1)

# Membuat slider dan label untuk nilai Indonesia
label_indonesia = tk.Label(root, text="Indonesia:")
label_indonesia.grid(row=4, column=0)
slider_indonesia = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_indonesia.grid(row=4, column=1)

# Membuat slider dan label untuk nilai kewarganegaraan
label_kewarganegaraan = tk.Label(root, text="Kewarganegaraan:")
label_kewarganegaraan.grid(row=5, column=0)
slider_kewarganegaraan = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_kewarganegaraan.grid(row=5, column=1)

# Membuat slider dan label untuk nilai kesenian
label_kesenian = tk.Label(root, text="Kesenian:")
label_kesenian.grid(row=6, column=0)
slider_kesenian = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_kesenian.grid(row=6, column=1)

# Membuat slider dan label untuk nilai sejarah
label_sejarah = tk.Label(root, text="Sejarah:")
label_sejarah.grid(row=7, column=0)
slider_sejarah = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_sejarah.grid(row=7, column=1)

# Membuat slider dan label untuk nilai PAI
label_pai = tk.Label(root, text="PAI:")
label_pai.grid(row=8, column=0)
slider_pai = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_pai.grid(row=8, column=1)

# Membuat slider dan label untuk nilai fisika
label_fisika = tk.Label(root, text="Fisika:")
label_fisika.grid(row=9, column=0)
slider_fisika = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_fisika.grid(row=9, column=1)

# Membuat slider dan label untuk nilai inggris
label_inggris = tk.Label(root, text="Inggris:")
label_inggris.grid(row=10, column=0)
slider_inggris = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider_inggris.grid(row=10, column=1)

# Membuat tombol submit
button_submit = tk.Button(root, text="Submit", command=submit_nilai)
button_submit.grid(row=11, column=0, columnspan=2)

# Membuat label untuk hasil prediksi
label_prediksi = tk.Label(root, text="Hasil Prediksi:")
label_prediksi.grid(row=12, column=0, columnspan=2)

# Menjalankan aplikasi
root.mainloop()
