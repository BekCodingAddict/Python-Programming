print(type(10))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>
print(type(len))         # <class 'builtin_function_or_method'>
print(type(type))        # <class 'type'>

def greet():
    print("hi")

x = greet   # assign function to variable
x()         # call it

print(callable(x))  # True

import math
print(type(math))  # <class 'module'>

try:
    1 / 0
except Exception as e:
    print(type(e))  # <class 'ZeroDivisionError'>

(10).bit_length()  # you can call methods on int
print((10).bit_length())  # you can call methods on float

print(type(type))
#print(help(int))

c=int('101',base=2)
print(c)

def cube(x):
	return x*x*x

def select_function(func_name):
	if func_name == 'cube':
		return cube
	else:
		return square

def square(x):
	return x*x


f = select_function('cube')

print(f is cube)


def do_something(func,arg):
	return func(arg)

print(do_something(cube,10))