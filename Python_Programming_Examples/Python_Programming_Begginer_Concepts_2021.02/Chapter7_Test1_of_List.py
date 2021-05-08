#리스트명= [값1,값2,값3]
aa=[10,20,30,40]
print(aa)
bb=[0,0,0,0]
sum=0
bb[0]=int(input("Imput the value to list[0] >>"))
bb[1]=int(input("Imput the value to list[1] >>"))
bb[2]=int(input("Imput the value to list[2] >>"))
bb[3]=int(input("Imput the value to list[3] >>"))
sum=bb[0]+bb[1]+bb[2]+bb[3]
print("Sum=%d"% sum)
cc=[]
for i in range (0,100):
    cc.append(0) ## 리스트명.append(값) 리스트에 값을 대입
len(cc); print("list size is %d"%len(cc)) ## len() 리스트 사이즈를 확인
## 합계를 계산하기
dd=[]
for i in range(0,10):
    dd.append(0)
sum=0
for i in range (0,10):
    dd[i]=int(input(str(i+1)+"변수 숫자 >>"))
    sum+=dd[i]
print("합계 >>%d,\u2665"% sum)