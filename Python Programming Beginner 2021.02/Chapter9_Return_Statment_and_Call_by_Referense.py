def func1():
    result=100
    return result
def func2():
    print("There is no return value!")
    return

print(func1());func2()
##The function that has a lot of return value
def func3(x,y):
    retlist=[]
    res1=x+y
    res2=x-y
    retlist.append(res1);retlist.append(res2)
    return retlist

div,sub=200,100
mylist=[]; mylist=func3(div,sub)
print("mylist[0]-->",(mylist[0])); print("mylist[1]-->",(mylist[1]))

if True:
    pass
else:
    print("False!")
##
def Func1(x,y):
    result=0
    result=x+y
    return result
def Func2(x,y,z):
    result=0
    result=x+y+z
    return result
print(Func1(10,20));print(Func2(10,20,10))

def Func3(x,y,z=0):
    result=0
    result=x+y+z
    return result
print(Func3(100,200))

