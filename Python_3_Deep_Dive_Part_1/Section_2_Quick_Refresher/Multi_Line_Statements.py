#implecit line continuation
#list 
a=[1,#item1 
2,3,4,5]
b=[6,7,8
,9,10]

c=(
	1,#item1
	2,#item2
	3,#item3
	4,#item4
	5,#item5
)
print(c[0])

#dictionary
d={
	"name":"John", # key1
	"age":30, # key2
	"city":"New York" # key3
}
print(d["name"])

#function
def add(a, #parameter1,
b #parameter2
):
	return a+b #return statement

print(add(1,2))

#explicit line continuation
a=1+2\
	+3+4+5+6+7+8+9+10
print(a)

a='''this  is a 
             multiline string 
                   line 2
'''
print(a)