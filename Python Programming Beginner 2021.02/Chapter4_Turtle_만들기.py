import turtle
import random

##declaration area of global variable
swidht,shight,pSize,exitCout=300,300,3,0
r,g,b,angle,dist,curX,Cury=[0]*7

##a part of main
turtle.title('맘대로 더니는 거북이')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidht+30,height=shight+30)
turtle.screensize(swidht,shight)

while True:
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))

    angle=random.randrange(0,360)
    dist=random.randrange(1,100)
    turtle.left(angle)
    turtle.forward(dist)
    curX=turtle.xcor()
    Cury=turtle.ycor()

    if(-swidht/2<=curX and curX<=swidht) and (-shight/2<=Cury and Cury<=shight/2):
        pass
    else:
        turtle.penup()
        turtle.goto()
        turtle.pendown()

        exitCout+=1
        if exitCout>=5:
            break
turtle.done()
