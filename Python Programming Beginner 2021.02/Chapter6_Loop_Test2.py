#heart impticon printing
print('\u2665')
i,j=0,0
for i in range (1,9):
    for j in range(1,7):
        print('\u2665',end="")
##
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
