from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
def speak():
    nilaiInt = float(nilaiMasuk.get())
    if nilaiInt >= 75.0:
        hasil = "Selamat Kamu lulus!"
    else:
        hasil = "Selamat kamu tidak lulus! Coba lagi besok!"
    
    myHasil.config(text=f"{hasil}")
# Design
root = tb.Window(themename="cyborg")
root.title("Nilai Kelulusan")
root.geometry('920x550')

# Judul
myJudul = tb.Label(text="Nilai Kelulusan", font=("Helvetica", 30), bootstyle="light")
myJudul.pack(pady=50)

# Entry
nilaiMasuk = tb.Entry(root, bootstyle="light")
nilaiMasuk.pack(pady=30)

# Button
myButton = tb.Button(root, bootstyle="light outline", text="SUBMIT", command=speak)
myButton.pack(pady=10)

# Hasil
myHasil = tb.Label(root, text="", font=("Helvetica", 25), bootstyle="light" )
myHasil.pack(pady=20)


root.mainloop()