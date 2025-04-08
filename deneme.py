import tkinter as tk
arayüz = tk.Tk()
arayüz.geometry("2000x1414") 
sekil = tk.PhotoImage(file="resim1.png")
etiket = tk.Label(arayüz ,image=sekil)
etiket.pack()
arayüz.mainloop()

