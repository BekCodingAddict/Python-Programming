Countries={}
country,city=0,0
number=0
number=int(input("Enter the Cuntries' number that you want to include>>"))
for i in range(0,number):
    country=str(input("%d.Enter the Country name>>"%(i+1)))
    city=str(input("%d. Enter the Capital name>>"%(i+1)))
    Countries[country]=city
print(Countries.keys()); mychoose=str(input("which country's capital do you want to know about?"))
if mychoose in Countries:
    print("<%s>'s capital is <%s> "%(mychoose,Countries.get(mychoose)))