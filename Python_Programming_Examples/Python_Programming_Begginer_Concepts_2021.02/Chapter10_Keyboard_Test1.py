from tkinter import*
from tkinter import messagebox

def keyevent(but):
    messagebox.showinfo("Ketboar Event","Are you sure delete this :"+chr(but.keycode))

window=Tk(); window.bind("<Delete>",keyevent); window.mainloop()