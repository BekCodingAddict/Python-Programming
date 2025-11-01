#Immutable Example (string)
def process(s):
	print(f'initial s #={id(s)}')
	s+="World"
	print(f'after s+="World" s #={id(s)}')

#s="Hello"
#print(f'outside s #={id(s)}')
#process(s)

#Mutable Example (list)
def modify_list(lst):
	print(f'initial lst #={id(lst)}')
	lst.append(4)
	print(f'after lst.append(4) lst #={id(lst)}')

#lst=[1,2,3]
#print(f'outside lst #={id(lst)}')
#modify_list(lst)

#Mutable Example (tuple)
def modify_tuple(tup):
	print(f'initial tup #={id(tup)}')
	tup[0].append(4)
	print(f'after tup[0].append(4) tup #={id(tup)}')

tup=([1,2],3)
print(f'outside tup #={id(tup)}')
modify_tuple(tup)
print(tup[0])