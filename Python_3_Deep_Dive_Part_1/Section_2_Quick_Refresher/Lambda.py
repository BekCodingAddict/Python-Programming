lambda_function = lambda x: x*2

print(lambda_function(2)) #4

def func(sqr,num):
	return sqr(num)

print(func(lambda_function,2)) #4
print(func(lambda x: x*3,2)) #6