import tkinter as tk
arayüz = tk.Tk()
arayüz.geometry("600x400") 
etiket = tk.Label(arayüz, text= "Küresel ısnmanın yıllık artışı")  
etiket.pack()
secim = tk.StringVar()
secim.set("yıl seç")
secenekler1=['2020' ,'2021', '2022','2023']
secim1 = tk.StringVar()
secim1.set("dil seç")
secenekler = ['az','tr']
dropdown = tk.OptionMenu(arayüz ,secim1 , *secenekler)
dropdown.pack()
dropdown = tk.OptionMenu(arayüz ,secim , *secenekler1)
dropdown.pack()
secim2 = tk.StringVar()
secim2.set("yıl seç")
secenekler2=['2021', '2022','2023','2024']
dropdown = tk.OptionMenu(arayüz ,secim2 , *secenekler2)
dropdown.pack()
resim=tk.PhotoImage(file =  "resim1.png")
resim1=tk.PhotoImage(file =  "resim.png")
resim2=tk.PhotoImage(file = "resim2.png")
resim3=tk.PhotoImage(file=  "resim3.png")
resim4=tk.PhotoImage(file=  "resim4.png")
resim5=tk.PhotoImage(file=  "resim5.png")
resim6=tk.PhotoImage(file=  "resim6.png")
resim7=tk.PhotoImage(file=  "resim7.png")
resim8=tk.PhotoImage(file=  "resim8.png")
resim9=tk.PhotoImage(file=  "resim9.png")
resim10=tk.PhotoImage(file="resim10.png")
resim11=tk.PhotoImage(file="resim11.png")
resim12=tk.PhotoImage(file="resim12.png")
resim13=tk.PhotoImage(file="resim13.png")
resim14=tk.PhotoImage(file="resim14.png")
resim15=tk.PhotoImage(file="resim15.png")
resim16=tk.PhotoImage(file="resim16.png")
resim17=tk.PhotoImage(file="resim17.png")
resim18=tk.PhotoImage(file="resim18.png")
resim19=tk.PhotoImage(file="resim19.png")
def yazdir():
    a = int(secim.get())
    b = int(secim2.get())
    c=secim1.get()
    if c=='tr':
        hata = tk.Label(arayüz,text='Birinci seçdiyin yıl ikinciden daha küçük olmalı')
        if a >= b:
            hata.pack()
        else:
            if a == int("2020") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                label = tk.Label(yil_penceresi, image=resim)
                label.pack()
            if a == int("2020") and b == int("2023"):
                yil_penceresi = tk.Toplevel(arayüz)
                kim = tk.Label(yil_penceresi, image=resim1)
                kim.pack()
            if a == int("2020") and b == int("2022"):
                yil_penceresi = tk.Toplevel(arayüz)
                tak = tk.Label(yil_penceresi, image=resim2)
                tak.pack()
            if a == int("2020") and b == int("2021"):
                yil_penceresi = tk.Toplevel(arayüz)
                tapa = tk.Label(yil_penceresi, image=resim3)
                tapa.pack()
            if a == int("2021") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                taa = tk.Label(yil_penceresi, image=resim4)
                taa.pack()
            if a == int("2021") and b == int("2023"):
                yil_penceresi = tk.Toplevel(arayüz)
                tssi = tk.Label(yil_penceresi, image=resim5)
                tssi.pack()
            if a == int("2021") and b == int("2022"):
                yil_penceresi = tk.Toplevel(arayüz)
                tap = tk.Label(yil_penceresi, image=resim6)
                tap.pack()
            if a == int("2022") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                tp = tk.Label(yil_penceresi, image=resim7)
                tp.pack()
            if a == int("2022") and b == int("2023"):
                yil_penceresi = tk.Toplevel(arayüz)
                minecraft = tk.Label(yil_penceresi, image=resim8)
                minecraft.pack()
            if a == int("2023") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                gtrr34 = tk.Label(yil_penceresi, image=resim9)
                gtrr34.pack()
    else:
        hat=tk.Label(arayüz,text='Birinci seçdiyin il ikincidən balaca olmalıdır')
        if a>=b:
            hat.pack()
        else:
            if a == int("2020") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                abel = tk.Label(yil_penceresi, image=resim10)
                abel.pack()
            if a == int("2020") and b == int("2023"):
                yil_penceresi = tk.Toplevel(arayüz)
                im = tk.Label(yil_penceresi, image=resim11)
                im.pack()
            if a == int("2020") and b == int("2022"):
                yil_penceresi = tk.Toplevel(arayüz)
                ak = tk.Label(yil_penceresi, image=resim12)
                ak.pack()
            if a == int("2020") and b == int("2021"):
                yil_penceresi = tk.Toplevel(arayüz)
                apa = tk.Label(yil_penceresi, image=resim13)
                apa.pack()
            if a == int("2021") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                aa = tk.Label(yil_penceresi, image=resim14)
                aa.pack()
            if a == int("2021") and b == int("2023"):
                yil_penceresi = tk.Toplevel(arayüz)
                tsi = tk.Label(yil_penceresi, image=resim15)
                tsi.pack()
            if a == int("2021") and b == int("2022"):
                yil_penceresi = tk.Toplevel(arayüz)
                ta = tk.Label(yil_penceresi, image=resim16)
                ta.pack()
            if a == int("2022") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                t = tk.Label(yil_penceresi, image=resim17)
                t.pack()
            if a == int("2022") and b == int("2023"):
                yil_penceresi = tk.Toplevel(arayüz)
                minecrat = tk.Label(yil_penceresi, image=resim18)
                minecrat.pack()
            if a == int("2023") and b == int("2024"):
                yil_penceresi = tk.Toplevel(arayüz)
                gtrr4 = tk.Label(yil_penceresi, image=resim19)
                gtrr4.pack()
button = tk.Button(arayüz, text="GİRİŞ", command=yazdir)
button.pack()
arayüz.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
