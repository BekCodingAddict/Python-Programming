tt=(10,20,30); print(tt); tt1=(10)#this is int tt1(10,)is tuple
print(tt1);print(type(tt1)); del(tt1)
tt1=(10,20,30,40); tt1[1]+tt1[2]+tt1[3];print(tt1)
print(tt1[1:3]);print(tt1[0::2]);del(tt1)
tt1=('A','B','C'); print("Tuple tt1*3>>",tt1*3); print("tuple tt+tt1>>",tt+tt1)
myTuple=(10,20,30,40); print("Begin of using list() function",myTuple)
myList=list(myTuple);print("After of using list() function ",myList)
myList.append(50); print(myList); myTuple=tuple(myList);print(myTuple)