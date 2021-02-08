import random
from tkinter.simpledialog import*

def getstring():
  retStr=""
  retStr=askstring('Enter words!','Enter the words that write the turtle!')
  return retStr
def RGB():
  r=random.random()
  g=random.random()
  b=random.random()
  return (r,g,b)
def getXYAS(sw,sh):
  x,y,ange,size=0,0,0,0
  x=-100##random.randrange(-sw/2,sw/2)
  y=-100#random.randrange(-sh/2,sh/2)
  ange=random.randrange(0,360)
  size=random.randrange(10,20)
  return [x,y,ange,size]