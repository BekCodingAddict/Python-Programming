a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
x = [1, 2, 3]
y = x  # y and x reference the same object

print(x == y)  # True  (same contents)
print(x is y)  # True  (same object)
a = 10000
b = 10000

print(a == b)  # True
print(a is b)  # False (usually)

a=None
b=None
print(a == b)  # True
print(a is b)  # True