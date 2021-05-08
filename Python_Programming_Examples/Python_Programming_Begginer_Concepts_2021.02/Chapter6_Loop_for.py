for i in range (0,3,1): #for 변수 in range (시작값,끝값+1,증가값):
    print("안녕하세용 저는 for 문을 공부 중입니다.^^")
for i in range (0,3,1):
    print("%d 회: 안녀하세요 for문을 공부 중입니다.^^"%i)
for i in range (2,-1,-1):
    print("%d 회: 안녀하세요 for문을 공부 중입니다.^^"%i)
for i in range (1,6,1):
    print("%d"%i,end=" ") #print("%d"%i, end=" " ->print  안에 있는 것들 i를 한 줄에 출력)
i,sum=0,0
for i in range (1,11,1):
    sum+=i
print("1 부터 10까지의 숫자들 합계는 %d 입니다.",sum)