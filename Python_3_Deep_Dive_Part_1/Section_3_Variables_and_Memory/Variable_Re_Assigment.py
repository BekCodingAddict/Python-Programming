a=10
print(hex(id(a))) #The id of a is 0x7f816c000000.
print(type(a)) #The type of a is <class 'int'>.
a=20
print(hex(id(a))) #The id of a is 0x7f816c000000. It has changed because the value of a has changed.
print(type(a)) #The type of a is <class 'int'>.
b=20
print(hex(id(b))) #The id of b is 0x7f816c000000. It is the same as the id of a because b is assigned the value of a.
print(hex(id(a))) #The id of a is 0x7f816c000000. It is the same as the id of b because a is assigned the value of b.
print(a is b) #True because a and b are the same object.
print(a == b) #True because a and b have the same value.
c=10
print(hex(id(c))) #The id of c is 0x7f816c000000. It is the same as the id of a because c is assigned the value of a.
print(hex(id(a))) #The id of a is 0x7f816c000000. It is the same as the id of c because a is assigned the value of c.
print(a is c) #True because a and c are the same object.
print(a == c) #True because a and c have the same value.
d=10
print(hex(id(d))) #The id of d is 0x7f816c000000. It is the same as the id of a because d is assigned the value of a.
print(hex(id(a))) #The id of a is 0x7f816c000000. It is the same as the id of d because a is assigned the value of d.
print(a is d) #True because a and d are the same object.
print(a == d) #True because a and d have the same value.