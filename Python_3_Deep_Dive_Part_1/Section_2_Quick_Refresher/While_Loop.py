#index = 0
#while index < 10:
#	print(index)
#	index += 1


#list = [10,20,30,40,50,60,70,80,90,100]
#index = 0
#while index < len(list):
#	print(list[index])
#	index += 1

#i = 0
#while True:
#	print("Hello World")
#	if i ==3:
#		break
#	i += 1

#min_length = 3
#name=input("Enter your name: ")
#while not(len(name)>=min_length and name.isalpha() and name.isprintable()):
#	name=input("Enter your name: ")

#print(f"Hello,{0}".format(name))

#Refactor the code to use a while loop
#while True:
#	name=input("Enter your name: ")
#	if len(name)>=min_length and name.isalpha() and name.isprintable():
#		break

#print(f"Hello,{name}".format(name))

# continue statement example
#a=0
#while a<10:
#	a+=1
#	if a%2==0:
#		continue
#	print(a)

# whileloop with if else statement
#list = [1,2,3,4,5,6,7,8]
#value = 10
#found = False
#index = 0
#while index < len(list):
#	if list[index] == value:
#		found = True
#		break
#	index += 1

#if not found:
#	list.append(value)	

#print(list)

# whileloop with else statement
list = [1,2,3,4,5,6,7,8]
value = 10
index = 0
while index < len(list):
	if list[index] == value:
		break
	index += 1
else:
	list.append(value)
	print("Value not found")

print(list)