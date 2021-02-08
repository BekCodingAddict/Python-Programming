import turtle
import random
##함수 선언 declarated functions
def screenLeftClick(x,y):
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidclick(x,y):
    global r,g,b
    tSize=random.randrange(1,10)
    turtle.shapesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()
# declarated variable
pSize,tSize=10,0
r,g,b=0.0,0.0,0.0
# Main function
turtle.title('Drawing by turtle')
turtle.shape('turtle')
turtle.pensize(tSize)
turtle.pensize(8)
turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidclick,2)
turtle.onscreenclick(screenRightClick,3)

turtle.done()
