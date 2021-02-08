
import turtle

i,k,tX,tY=[0]*4
sweidth,shight=800,500

##main
if __name__ == "__main__":
    turtle.title('거북이 구두단')
    turtle.shape('turtle')
    turtle.setup(width=sweidth+50,height=shight+50)
    turtle.screensize(sweidth,shight)
    turtle.penup()
    turtle.speed(10)
    tX,tY=-500,250
    turtle.goto(tX,tY)

    for i in range(1,10):
        for k in range (2,10):
            turtle.goto(tX+80*k,tY-40*i)
            gugu=str(k)+'x'+str(i)+'='+str(k*i)
            turtle.write(gugu,font=('Arial',12,'bold'))
    turtle.done()
