a=10
b=10
print(f'a #={id(a)}') #same id because integer is immutable
print(f'b #={id(b)}') #same id because integer is immutable

string_a="Hello"
string_b="Hello"
print(f'string_a #={id(string_a)}') #same id because string is immutable
print(f'string_b #={id(string_b)}') #same id because string is immutable

list_a=[1,2,3]
list_b=[1,2,3]
print(f'list_a #={id(list_a)}') #different id because list is mutable
print(f'list_b #={id(list_b)}') #different id because list is mutable

name="John"
age=30
Job="Engineer"
person={
	"name":name,
	"age":age,
	"Job":Job
}

print(f'person #={id(person)}') #same id because dictionary is mutable
person["name"]="Jane" #change the value of the dictionary
print(f'person #={id(person)}') #same id because dictionary is mutable
print(person["name"]) #print the value of the dictionary
print(name) #print the value of the variable

aa=500
bb=500
print(f'aa #={id(aa)}') #same id because integer is immutable
print(f'bb #={id(bb)}') #same id because integer is immutable
