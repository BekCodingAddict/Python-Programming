from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(5, Iterable))          # False


my_list = [10, 20, 30]
it = iter(my_list)

print(next(it))  # 10
print(next(it))  # 20
print(isinstance(it, Iterable))  # True

for i in range(3):
	print(i)

print(list	(range(3)))

for i in range(15):
	print(i)
	if i%7==0:
		print("Multiple of 7 found")
		break
else:
	print("No multiple of 7 found")


for i in range(5):
	print("-------------")
	try:
		10/(i-3)
	except ZeroDivisionError:
		print("Division by zero")
		continue
	finally:
		print("Finally block executed")
	
else:
	print("No exception occurred")