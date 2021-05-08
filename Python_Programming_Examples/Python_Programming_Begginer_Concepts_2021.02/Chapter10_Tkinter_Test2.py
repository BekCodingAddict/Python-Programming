from tkinter import*
from tkinter import messagebox
mywin=Tk(); mywin.geometry('800x500');mywin.title('Python Widget');##photo=PhotoImage(file="A:\Gifpic4.GIF")

button2=Button(mywin,text="Button 1"); button3=Button(mywin,text="Button 2"); button4=Button(mywin,text="Button 3");
button2.pack(side=LEFT);button3.pack(side=LEFT); button4.pack(side=LEFT)

var=IntVar()


def myFunc1():
  if var.get()==1:
    label2.configure(text="Python is very easy and powerful programming language!")
  elif var.get()==2:
    label2.configure(text="C++ is a gread programming \n language for game and embedded system engineering!")
  else:
    label2.configure(text="JavaScript is very popular programming language for wep development!")

rb1=Radiobutton(mywin,text="Python",variable=var,value=1,command=myFunc1)
rb2=Radiobutton(mywin,text="C++",variable=var,value=2,command=myFunc1)
rb3=Radiobutton(mywin,text="JavaScript",variable=var,value=3,command=myFunc1)

label1=Label(mywin,text="Do you want to close click here ",font=("Check",10)); label1.pack(side=BOTTOM)
button1=Button(mywin,text="CLOSE",command=quit);button1.pack(side=BOTTOM)

label2=Label(mywin,text="Which Programming language are you learning?",)

rb1.pack(side=BOTTOM);rb2.pack(side=BOTTOM);rb3.pack(side=BOTTOM);label2.pack(side=BOTTOM)





mywin.mainloop()