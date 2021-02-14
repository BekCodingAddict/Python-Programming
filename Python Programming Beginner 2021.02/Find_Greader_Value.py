from abc import abstractmethod


a=0;b=0
a=int(input("Enter the value for a >> "))
b=int(input("Enter the value for b >> "))
sum=a;sum2=0
while a<b:
  sum=sum*(a+1)
  print(a)
  a+=1
if a%2==0:
  print("Sum >>",(sum/2))
else:
  print("Sum >>",sum)

