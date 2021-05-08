from tkinter import*
from tkinter import messagebox
from typing import Sized

window=Tk();window.title("Python Windows Programming"); window.geometry('800x500')
# photo=PhotoImage(file="A:\Gifpic5.GIF"); label1=Label(window,image=photo);label1.pack()

btlist=[None]*3
for i in range(0,3):
  btlist[i]=Button(window,text="Button "+str(i+1))
for btn in btlist:
  btn.pack(side=TOP,fill=X,padx=350,pady=10,ipadx=10,ipady=10)
window.mainloop()