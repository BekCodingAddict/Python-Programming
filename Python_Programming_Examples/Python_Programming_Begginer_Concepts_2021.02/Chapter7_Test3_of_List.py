myList=[20,10,30,40]; print(" The exist List>>%s"%myList) 
myList.append(50); print("later append(50) used The exist List>>%s"%myList)#listname.append(value) add the value finally place
print("pop()으로 추출한 값 >>%s"% myList.pop()); print("later pop() was used list >>%s"%myList) # listname.pop() Ohirgi kiritilgan qiymatni ochradi

myList.sort(); print("After sort() is used list >>%s"% myList) # List qiymatini sort qiladi

myList.reverse(); print(" After reverse() is used List>>%s",myList)# reverse() teskarisiga sort qiladi 

print("20 값의 위치 확인 : %d"% myList.index(20))# list manzilini aniqlash uchun index(qiymat)

myList.insert(5,50); myList.sort(); print("After insert() is used list >>%s",myList) #insert() can add the value to list index

myList.remove(50); print("After remove() is used List >>%s"% myList) ##remuve()can delete the value that was inputed inside it

myList.extend((77,78,79)); print("After extend() is used List >>%s"%myList) # extend() can add a list to another list

aa=[20,10,30]; myList=sorted(aa); print(myList)# sorted can sort the list after copyed information to another list

