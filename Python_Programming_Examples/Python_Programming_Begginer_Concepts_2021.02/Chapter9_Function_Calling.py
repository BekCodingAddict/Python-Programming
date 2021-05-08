def func1(*para):
    result=0
    for num in para: ## avtomatichski num=0 para ga 2 ta qiymat kiritilsa para=2 boladi
        result+=num
    return result

print(func1(1.5,1.5,1.5)); print(func1(10,10,10))##print(func1('A','B','C'))--> this is error
## **variable bolsa dictonaryga aylanadi
def func2(**para):
    for k in para.keys():
        print("%s-->%s people!"%(k,para[k]))

func2(friends=9,Otabek=23,area=1.23,Name="seoul")
##
import random
def getnum():
    return random.randrange(1,46)
lotto=[];lotto1=[]
num=0
print("Lotto is getting start!")
for i in range(1,7):
    num=int(input("Enter %d number for Lotto>>"%i))
    lotto1.append(num)
while True:
    lnum=getnum()
    if lotto.count(lnum)==0:
        lotto.append(lnum)
    if len(lotto)>=6:
        break
lotto.sort()
print("The gift numbers>>",lotto,end="")
lotto1.sort();print("\n")
if lotto1==lotto:
    print("You win!!")
else:
    print("You lose!!")

