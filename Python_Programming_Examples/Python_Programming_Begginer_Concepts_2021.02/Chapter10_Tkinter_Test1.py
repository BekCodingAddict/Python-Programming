from tkinter import*
from tkinter import messagebox
def massBox():
  messagebox.showinfo('CLOSE PYTHON BOTTON','Python is very easy,isn"t it?')

def messBox1():
  if chk.get()==0:
    messagebox.showinfo('','Check Botton Turned Off')
  else: 
    messagebox.showinfo('','Check Botton Turned on')

if __name__=="__main__":
  window=Tk()
  photo=PhotoImage(file="A:\Gifpic.GIF")
  window.geometry('800x500')
  label1=Label(window,image=photo)

  chk=IntVar()
  cb1=Checkbutton(window,text="Click here On/Off ",variable=chk,command=messBox1,anchor=CENTER)
  cb1.pack()

  button1=Button(window,text="CLOSE PYTHON",command=massBox)
  button1.pack()
  label1.pack()
  window.mainloop()