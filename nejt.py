import tkinter as tk
from PIL import Image, ImageTk  # Pillow kütüphanesi
def resim():
    pencere = tk.Tk()
    pencere.title("Fotoğraf Gösterme")

    image = Image.open("resim.jpg")  # JPG, PNG vs. olur
    image = image.resize((300, 200))  # İsteğe bağlı boyutlandırma

    resim = ImageTk.PhotoImage(image)

    etiket = tk.Label(pencere, image=resim)
    etiket.pack()

    pencere.mainloop()
