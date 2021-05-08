import turtle
import random

#전역 변수 선언 부분
myTurtle,tX,tY,tColor,tsize,tShape=[None]*6
shapeList=[];playerTurtles=[]
swidth,shight=800,500
##메인 변수 부분
if __name__ == "__main__":
    turtle.title('Using way of list with Turtle graphic library')
    turtle.setup(width=swidth+50,height=shight+50)
    turtle.screensize(swidth,shight)

    shapeList=turtle.getshapes()
    for i in range (0,100):
        random.shuffle(shapeList)
        myTurtle=turtle.Turtle(shapeList[0])
        tX=random.randrange(-swidth/2,swidth/2)
        tY=random.randrange(-shight/2,shight/2)
        r=random.random(); g=random.random(); b=random.random()
        tsize=random.randrange(1,3)
        playerTurtles.append([myTurtle,tX,tY,tsize,r,g,b])
    for tList in playerTurtles:
        myTurtle=tList[0]
        myTurtle.color(tList[4],tList[5],tList[6])
        myTurtle.pencolor(tList[4],tList[5],tList[6])
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1],tList[2])
    turtle.done()