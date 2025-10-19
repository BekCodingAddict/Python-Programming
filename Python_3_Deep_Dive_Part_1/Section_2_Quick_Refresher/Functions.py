list = [1,2,3,4,5]
print(len(list))
print(max(list))
print(min(list))
print(sum(list))
print(sorted(list))
print(reversed(list))


from math import sqrt

print(sqrt(16))
print(pow(2,3))
print(abs(-10))
print(round(3.14))


def function_1():
	print('running function_1')

function_1()

def function_2(a,b):
	return a*b

print(function_2(2,3))
print(function_2("a",5))
#print(function_2("a","b")) TypeError: can't multiply sequence by non-int of type 'str'
#print(function_2(1,2,3)) #TypeError: function_2() takes 2 positional arguments but 3 were given
print(function_2([1,2,3],2)) #TypeError: can't multiply sequence by non-int of type 'list'
print(function_2((1,2,3),2)) #TypeError: can't multiply sequence by non-int of type 'tuple'
print(function_2(True,2)) #TypeError: can't multiply sequence by non-int of type 'bool'
print(function_2(False,2)) #TypeError: can't multiply sequence by non-int of type 'bool'
#print(function_2(None,2)) #TypeError: can't multiply sequence by non-int of type 'NoneType'
#print(function_2(0,2)) #TypeError: can't multiply sequence by non-int of type 'int'
#print(function_2(0.0,2)) #TypeError: can't multiply sequence by non-int of type 'float'
#print(function_2({"a":1,"b":2},2)) #TypeError: can't multiply sequence by non-int of type 'dict'

def func():
	return func_2()

def func_2():
	return " running func_2"

print(func()) #running func_2

def func_3():
	return func_4()

print(func_3()) #NameError: name 'func_4' is not defined

def func_4():
	return "running func_4"