#Using way of while loop
'''번수=시작값
while 변수<끝값:
    이 부분 반복
    변수=변수 +증가값'''
i=0
while i<3:
    print("%d 회 : 저는 while 반복문을 공부 중입니다!"%i)
    i+=1
##무한 loop
print("중지하려면 Ctrl+ c 눌러 주세요!")
ch=""
a,b=0,0
while True: # while 조건문이 true이면 무한대로 반복된다;
   a=int(input("계산할 첫번째 숫자를 입력해 주세요!"))
   b=int(input("계산할 두번째 숫자를 입력해 주세요!"))
   ch=input("계산할 연산자를 입력하세요!")
   if(ch=="+"):
       print("%d+%d=%d"%(a,b,a+b))
   elif(ch=="-"):
        print("%d-%d=%d"%(a,b,a-b))
   elif(ch=="*"):
        print("%d*%d=%d"%(a,b,a*b))
   elif(ch=="/"):
        print("%d/%d=%d"%(a,b,a/b))