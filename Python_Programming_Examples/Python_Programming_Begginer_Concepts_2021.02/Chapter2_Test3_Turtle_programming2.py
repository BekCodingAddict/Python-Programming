import turtle

#함수 선언 부분

#변수 선언 부분
myT=None

## Main code area
myT=turtle.Turtle()
myT.shape('turtle')
for i in range(0,100):
    myT.forward(20)
    myT.right(5)

turtle.done()