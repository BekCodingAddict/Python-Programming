from tkinter import*
from tkinter import messagebox

def clickLeft(event):
  messagebox.showinfo('Mause','Cliced the left button!')

window=Tk();window.geometry('800x500'); photo=PhotoImage(file="A:\\Gifpic4.GIF")
# window.bind("<Button-1>",clickLeft)
lable1=Label(window,image=photo)
lable1.bind("<Button>",clickLeft)
lable1.pack(expand=1,anchor=CENTER)
window.mainloop()