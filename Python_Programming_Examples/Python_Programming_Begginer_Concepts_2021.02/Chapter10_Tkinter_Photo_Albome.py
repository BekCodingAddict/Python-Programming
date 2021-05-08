from tkinter import*
from time import*

fnameList=["Gifpic.GIF","Gifpic2.GIF","Gifpic3.GIF","Gifpic4.GIF","Gifpic5.GIF"]
photoList=[None]*5;num=0

def clickNext():
  global num; num+=1
  if num>8: 
    num=0
  photo=PhotoImage(file="A:\\"+fnameList[num]); 
  plable.configure(image=photo); plable.image=photo

def clickPrev():
  global num; num-=1
  if num<0:
    num=8
  photo=PhotoImage(file="A:\\"+fnameList[num]);
  plable.configure(image=photo); plable.image=photo

myWin=Tk(); myWin.geometry('830x600'); myWin.title("Python Photo Albom")
btnPrev=Button(myWin,text="<<Previos",command=clickPrev); btnNext=Button(myWin,text="Next>>",command=clickNext)
photo=PhotoImage(file="A:\\"+fnameList[0])
plable=Label(myWin,image=photo); btnPrev.place(x=280,y=15); btnNext.place(x=460,y=15)
plable.place(x=15,y=50)
myWin.mainloop()