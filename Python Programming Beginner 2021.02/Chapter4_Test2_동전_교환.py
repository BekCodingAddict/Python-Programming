money,w500,w100,w50,w10=0,0,0,0,0

#메인 함수
money=int(input("How much do you want to change money?"))
w500=money//500
money%=500

w100=money//100
money%=100

w50=money//50
money%=50

w10=money//10
money%=10

print(" w500 cash is %d\n"% w500)
print(" w100 cash is %d\n"% w100)
print("w50 cash is %d\n"% w50)
print(" w10 cash is %d\n"% w10)
print("don't change money id %d\n"% money)