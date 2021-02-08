list1=[]; list2=[]; value=1
for i in range(0,3):
    for k  in range (0,4):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]
for i in range (0,3):
    for k in range(0,4):
        print("%3d"%list2[i][k],end="")
    print("")
list3=[];list4=[];value2=0
for i in range (0,4):
    for j in range( 0,5):
        list3.append(value2)
        value2+=3
    list4.append(list3)
    list3=[]
for i in range(0,4):
    for j in range(0,5):
        print("%3d"%list4[i][j],end="")
    print("")