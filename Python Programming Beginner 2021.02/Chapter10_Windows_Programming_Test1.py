from tkinter import* 

window=Tk()##Tkinter Tk funksiyasi windowsga chaqirildi
window.title('Window''s title')
window.geometry('800x500')
##windows.resizable(width=False,height=False)

label2=Label(window,text="Powerful ",font=("궁서체",50),fg='green')
label3=Label(window,text="Programming Language!!!",font=("Molla",50),bg="magenta",width=800,height=500,anchor=CENTER)
label1=Label(window,text="COOCBOOK~~~Python is",font=("red",40),fg='red')

label1.pack()
label2.pack()
label3.pack()
window.mainloop()