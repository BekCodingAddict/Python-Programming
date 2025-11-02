a = "hello"
b = "hello"
print(a is b)  # True  — same memory object

x = "".join(["he", "llo"])
print(x == a)  # True  — same value
print(x is a)  # False — different objects

import sys

a = sys.intern("hello world")
b = sys.intern("hello world")
print(a is b)  # True

a = 100
b = 100
print(a is b)  # True

x = 300
y = 300
print(x is y)  # False  (likely, depending on implementation)

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 is t2)  # False (no automatic interning here)

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))  # might be same if optimized by compiler

a=10
b=int(10)
c=int('10')
d=int('1010',2)
print(id(a), id(b), id(c), id(d))
