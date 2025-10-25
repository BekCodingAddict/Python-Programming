#a=10
#b=0

#try:
#	a/b
#except ZeroDivisionError:
#	print("Error: Division by zero")

#finally:
#	print("Finally block executed")

a=0
b=10

while a<4:
	print("---------------")
	a+=1
	b-=1

	try:
		a/b
	except ZeroDivisionError:
		print(f"{0},{1} - Division by zero".format(a,b))
		break
	finally:
		print(f"{0},{1} - Always executes".format(a,b))

	print(f"{0},{1} - After try-except block".format(a,b))
else:
	print("No exception occurred")