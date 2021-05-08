Pstring="Python great"; print("Pstring==>%s"%Pstring); print("Pstring==>%s"%Pstring[0])
print("Pstring=>>%s"%Pstring[1:5]);print("Pstring==>>",Pstring[4:])
Pstring+'Programming Language'; print("Pstring used + operator >>",Pstring)
print(len(Pstring))
slen=len(Pstring)
for i in range(0,slen):
    print(Pstring[i]+'+')
##Testkari print dasturi
instr,outstr="",""
count,i=0,0
instr=input("Enter the string!")
count=len(instr)
for i in range(0,count):
    outstr+=instr[count-(i+1)]
print("\n")
print("Testkari Prit==>",outstr)