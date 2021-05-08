from tkinter import*
from tkinter.simpledialog import*

window=Tk(); window.geometry('800x500')
label1=Label(window,text="Impeted value")
label1.pack()

value=askinteger("확대 배수","1-6 imput the numer 1-6:",minvalue=1,maxvalue=6)

label1.configure(text=str(value))
window.mainloop()