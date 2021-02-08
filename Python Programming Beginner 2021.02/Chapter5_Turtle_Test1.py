import turtle
import math
import random

##전역 변수 영역
t1,t2,t3=[None]*3
t1X,t1Y,t2X,t2Y,t3X,t3Y=[0]*6
swidth,sheight=800,500
##메인 코드 부분
if __name__ == "__main__":
    turtle.title("The Meeting Turtles witsh each others")
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)

    t1=turtle.Turtle('turtle'); t1.color('red'); t1.penup()
    t2=turtle.Turtle('turtle'); t2.color('green'); t2.penup()
    t3=turtle.Turtle('turtle'); t3.color('blue'); t3.penup()
    t1.goto(-100,-100);t2.goto(0,0); t3.goto(100,100)
    t1.speed(1);t2.speed(1)

    while True:
        angle =random.randrange(0,360)
        dist=random.randrange(1,50)
        t1.left(angle); t1.forward(dist)
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t2.left(angle); t2.forward(dist)
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t3.left(angle); t3.forward(dist)

        t1X=t1.xcor();t1Y=t1.ycor()
        t2X=t2.xcor(); t2Y=t2.ycor()
        t3X=t3.xcor(); t3Y=t3.ycor()

        if math.sqrt(((t1X-t2X)*(t1X-t2X))+((t1Y-t2Y)*(t1X-t2Y))) <=20 or\
            math.sqrt(((t1X-t3X)*(t1X-t3X))+((t1Y-t3Y)*(t1X-t3Y))) <=20 or\
            math.sqrt(((t2X-t3X)*(t2X-t3X))+((t2Y-t3Y)*(t2X-t3Y))) <=20:
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
            break

turtle.done()