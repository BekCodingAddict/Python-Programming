#x = [1, 2, 3]
#print(id(x))       # e.g., 140034380229376
#x.append(4)
#print(id(x))       # same ID → mutated in place

#y = "Hello"
#print(id(y))       # e.g., 140034380158512
#y += " World"
#print(id(y))       # new ID → new string createda = [1, 2, 3]

#a = [1, 2, 3]
#b = a

#b.append(4)
#print(a)  # [1, 2, 3, 4]
#print(a is b)  # True

#a = "Hi"
#b = a
#b += "!"
#print(a)  # "Hi"
#print(b)  # "Hi!"
#print(a is b)  # False
#import copy
#x = [1, 2, 3]
#y = x
#y.append(4)
#print(x)  # [1, 2, 3, 4]
#y = copy.deepcopy(x)
#y.append(5)
#print(x)  # [1, 2, 3, 4]
#print(y)  # [1, 2, 3, 4, 5]
#print(x is y)  # False


#def modify_list(lst):
#    lst.append(100)

#def modify_int(n):
#    n += 100

#nums = [1, 2, 3]
#x = 10

#modify_list(nums)
#modify_int(x)

#print(nums)  # [1, 2, 3, 100]  (mutated)
#print(x)     # 10  (unchanged)
#my_dict = { (1, 2): "ok" }   # ✅ tuple is immutable
##my_dict = { [1, 2]: "error" } # ❌ list is mutable → TypeError

##Mutable Example
#class Counter:
#    def __init__(self, value=0):
#        self.value = value
#    def increment(self):
#        self.value += 1

##Immutable Example
#class Point:
#    def __init__(self, x, y):
#        self._x = x
#        self._y = y
#    def __setattr__(self, name, value):
#        if hasattr(self, name):
#            raise AttributeError("Immutable!")
#        super().__setattr__(name, value)


#tuple_example = (1, 2, 3)
#print(id(tuple_example))
#a=[1,2,3]
#b=[4,5,6]

#t=(a,b)
#print(id(t))
#a.append(7)
#b.append(8)
#print(t)  # [(1, 2, 3, 7), (4, 5, 6, 8)]
#print(id(t))

my_list=[1,2,3]
my_list_2=my_list+[4,5,6]
print(my_list)  # [1, 2, 3]
print(id(my_list))
print(my_list_2)  # [1, 2, 3, 4, 5, 6]
print(id(my_list_2))