import turtle
##전역 변수 선언부분
swidth,sheight=800,500
##메인 코드 부분
if __name__ == "__main__":
    turtle.title('Drawing rainbow')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50,height=sheight+50)## screen size install
    turtle.screensize(swidth,sheight)## scrensize
    turtle.penup()
    turtle.pensize(10)
    turtle.goto(0,-sheight/2) ## 거북이 이독시키는 함수 goto(weidth,height)
    turtle.pendown()
    turtle.speed(20)
    for radius in range(1,100):
        radius*=4
        if radius%7==1:
            turtle.pencolor('red')
        elif radius%7==2:
            turtle.pencolor('orange')
        elif radius%7==3:
            turtle.pencolor('yellow')
        elif radius%7==4:
            turtle.pencolor('green')
        elif radius%7==5:
            turtle.pencolor('blue')
        elif radius%7==6:
            turtle.pencolor('navyblue')
        else:
            turtle.pencolor('purple')
        turtle.circle(radius)

turtle.done()