import random
import math

random_number = math.floor(random.random() * 100)
print(random_number)

#if statement
if random_number>50:
	print("You are lucky")
elif random_number<50:
	print("You are not lucky")
else:
	print("You are very lucky")

#match statement
match random_number:
    case _ if random_number>50:
        print("You are lucky")
    case _ if random_number<50:
        print("You are not lucky")
    case _ if random_number==50:
        print("You are very lucky")

#ternary operator
result = "You are lucky" if random_number>50 else "You are not lucky" if random_number<50 else "You are very lucky"
print(result)

