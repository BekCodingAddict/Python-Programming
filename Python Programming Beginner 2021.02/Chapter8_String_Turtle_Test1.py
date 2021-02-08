import turtle
import random
from tkinter.simpledialog import*
##local variable
instr=" "
swidth,sheight=800,500
tx,ty,txtsize=[0]*3
##main 
turtle.title('Writing turtle!')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
instr=askstring("Enter the string:","Enter the string that write turtle")
turtle.speed(1)
for ch in instr:
    tx=random.randrange(-swidth/2,swidth/2)
    ty=random.randrange(-sheight/2,sheight/2)
    a=random.random();b=random.random();c=random.random()
    txtsize=random.randrange(10,50)

    turtle.goto(tx,ty)
    turtle.pencolor((a,b,c))

    turtle.write(ch,font=('맑은 고딕',txtsize,'bold'))

turtle.done()