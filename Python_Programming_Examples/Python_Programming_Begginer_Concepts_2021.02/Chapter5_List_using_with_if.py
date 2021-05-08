fruit=['Apple','Pear','Straberry','Grape']
print(fruit); fruit.append('Orange')
print(fruit)
if 'Orange' in fruit:
    print("There is an Orange!")
import random

number=[]
for num in range(0,10):
    number.append(random.randrange(0,10))

print("The Created list are",number)
for num in range(0,10):
    if num not in number:
        print("The number %d not exist in list"%num)