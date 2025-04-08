import tkinter as tk
arayüz = tk.Tk()
arayüz.geometry("600x400") 
etiket = tk.Label(arayüz, text= "Küresel ısnmanın yıllık artışı")  
etiket.pack()
secim = tk.StringVar()
secim.set("yıl seç")
secenekler1=['2020' ,'2021', '2022','2023']
dropdown = tk.OptionMenu(arayüz ,secim , *secenekler1)
dropdown.pack()
secim2 = tk.StringVar()
secim2.set("yıl seç")
secenekler2=['2021', '2022','2023','2024']
dropdown = tk.OptionMenu(arayüz ,secim2 , *secenekler2)
dropdown.pack()
haber = False
def yazdir():
    haber=False
    a = int(secim.get())
    b = int(secim2.get())
    hata = tk.Label(arayüz,text='Birinci seçdiyin yıl ikinciden daha küçük olmalı')
    yil = tk.Tk()
    im = tk.PhotoImage(file="resim1.png")
    label = tk.Label(yil, image=im)
    if a >= b:
        hata.pack()
    else:
        haber =True
        label.pack()
        yil.mainloop()
button = tk.Button(arayüz, text="GİRİŞ", command=yazdir)
button.pack()
arayüz.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                