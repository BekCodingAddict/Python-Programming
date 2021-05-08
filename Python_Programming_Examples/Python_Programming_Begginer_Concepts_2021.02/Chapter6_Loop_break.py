sum=0
a,b=0,0
while True:
    a=int(input("Imput the value to A"))
    b=int( input("input(Impt the value t B"))
    if (a==0)or (b==0):
        print("You impued 0 because the program has finished!")
        break## 조건이 참이면 반복문이 종료시켜 줌
    sum=a+b; print("%d+%d=%d"%(a,b,sum))
sum,i=0,0
for i in range(1,100):
    sum+=i
    if sum>=1000:
        print("1 dan boshlab ozoro qoshilgan sonlar qiymati 1000ga tenglashdi!")
        break
print("1-100  gacha sonlar orasida %d toxtalish boldi!"% i)
    