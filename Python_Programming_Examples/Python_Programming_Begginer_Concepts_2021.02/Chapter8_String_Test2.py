pstr="Python is ver easy"; print(pstr.upper());print(pstr.lower())
print(pstr.swapcase());print(pstr.title())
ss="Python ver very easy!"
print(ss.count('very')); print(ss.find('!'));print(ss.rfind('!'))
print(ss.index('Python')); print(ss.endswith('Python')); print(ss.startswith('Python'))
##stringni qavs bilan oraberuvchi program tuzish
ss=input("Enter the string>>"); print(ss)
if ss.startswith('<<')==False:
    print("<<",end="")
print(ss,end='')
if ss.endswith(">>")==False:
    print(">>",end="")
print("\n")
aa='<<<<P  y  t  h  o  n>>>$'; print(aa.strip());print(aa.rstrip()); print(aa.lstrip())
print(aa.strip('<>$'))## Strip can delete any operator where is in strip()
## Deleting free places where is in string
bb="  Python Programming is cool!"
cc=''
for i in range(0,len(bb)):
    if bb[i]!="":
        cc+=bb[i]

print(bb); print(cc)
##Replace function
qq="I'm learn Python hard!"
print(qq.replace('Python','C++')); print(qq)
##Second EXAMPLE
ww="Python has a lot of lybrary!"
print(ww,end="")
for i in range (0,len(ww)):
    if ww[i]!="":
        print(ww[i],end="")
        
    else:
        print("+",end=""); print(ww.replace("","+"))
