sum,i=0,0
for i in range(1,101):
    if i%3==0:
        print("%d의 3으로 나머지 값이 0입니다!"%i)
        continue
    sum+=i
print("1-100의 합계 (3의 배수 제외): %d"%sum)
sum,i=0,0
for i in range(1,101):
    sum+=i; print("i=%d"%i)
    if i==50:
        i=i-48; print("I 50 ga tenglashdi")
        continue
    if i==80:
        print("i 80 ga tenglashdi")
        break