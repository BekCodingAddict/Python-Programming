my_var = 10
print(my_var)
print(id(my_var))
print(hex(id(my_var)))
greeting="Hello, World!"
print(greeting)
print(id(greeting))
print(hex(id(greeting)))

a=[1,2,3]
b=a #Both a and b point to the same memory location.
a.append(4)
print(b)

#Mutable vs Immutable Objects
a=10
b=a
a=a+1
print(a) #a is now 11 because it is a mutable object.
print(b) #b is still 10 because it is an immutable object.

#Checking References
a=[1,2,3]
a.append(4)
b=a
print(b)
c=[1,2,3]
print(a is b) #True because a and b point to the same memory location.
print(a is c) #False because a and c point to different memory locations.
print(id(a),id(b),id(c)) #The ids of a and b are the same because they point to the same memory location, while the id of c is different because it points to a different memory location.

#Passing Objects to Functions
def modify_list(lst):
	lst.append(4)

my_list=[1,2,3]
modify_list(my_list)
print(my_list) #The list is now [1,2,3,4] because the function modified the list.

name="John"
last_name="Doe" + " " + name
print(last_name) #The last name is "John Doe" because the function modified the string.
full_name=last_name+" "+"Smith"
print(full_name) #The full name is "John Doe" because the function modified the string.