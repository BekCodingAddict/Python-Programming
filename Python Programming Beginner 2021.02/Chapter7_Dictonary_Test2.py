foods={}
name,dif=0,0

for i in range(0,3):
    name=str(input("%d.Enter food name>>"%i))
    dif=str(input("%d. Enter dif name>>"%i))
    foods[name]=dif
print(foods)
while (True):
    myfood=input(str(list(foods.keys()))+" what would you like??")
    if myfood in foods:
        print("<%s> ovqati <%s> bilan yeyilsa mazali!"%myfood,foods.get(myfood))
    elif myfood=="end":
        break
    else:
        print("There is no such as foos.Please check again!")

