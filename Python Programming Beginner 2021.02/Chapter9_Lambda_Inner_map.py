from typing import NewType


def outFunc(num1,num2):
  def inFunc(n1,n2):
    return(n1+n2)
  return inFunc(num1,num2)

print(outFunc(10,10))
##Lambda function
sum=lambda num1,num2:num1+num2
print(sum(20,20))
sum2=lambda num1=100,num2=200:num1+num2
print(sum2()); print(sum2(200,200))

myList=[1,2,3,4,5];print(myList)
def add10(num):
  return num+10
for i in range(len(myList)):
  myList[i]=add10(myList[i])
print(myList)
##LAmbda bilan qisqaroq
sum2=lambda num1:num1+10
myList=list(map(sum2,myList))
print(myList)
##Anodther way
myList=list(map(lambda num1:num1+10,myList))
print(myList)
##

List1=[1,2,3,4,5]; List2=[10,20,30,40,50]
newList=list(map(lambda num1,num2:num1+num2,List1,List2))
print(newList)
# ##Recursion Function


def count(num1):
  if num1>=1:
    print(num1,end='')
    count(num1-1)
  else:
    return
count(10)
count(20)
def factorial(num):
  if num<=1:
    return num
  else:
    return num*factorial(num-1)
print("\n")
print(factorial(5))
##yeld
def genFunc():
  yield 1
  yield 2
  yield 3
print(list(genFunc()))