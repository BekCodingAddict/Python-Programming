string1="hello world"
string2="hello world"
print(string1 is string2)

import sys
a=sys.intern("hello world")
b=sys.intern("hello world")
c="hello world"
print(a is b)
print(a is c)

def compare_using_equals(n):
	a="a long string that is not interned"
	b="a long string that is not interned"
	for i in range(n):
		if a == b:
			pass	

def compare_using_interning(n):
	a=sys.intern("a long string that is not interned")
	b=sys.intern("a long string that is not interned")
	for i in range(n):
		if a is b:
			pass

import time
start=time.perf_counter()
compare_using_equals(10000000)
end=time.perf_counter()
print(f"Time taken: {end-start} seconds")
print("--------------------------------")
start=time.perf_counter()
compare_using_interning(10000000)
end=time.perf_counter()
print(f"Time taken: {end-start} seconds")
