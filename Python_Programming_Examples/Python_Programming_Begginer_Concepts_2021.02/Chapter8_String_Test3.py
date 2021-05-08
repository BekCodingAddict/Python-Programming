##using map()
before=['2021','01','31']; after=list(map(int,before))
print(after); print("After is ",type(after[0]),"Before is ",type(before[0]))
## You can see the data type of list has changed from string to int
#center() can add free place after the string
aa="Python"
print(aa.center(100)); print(aa.center(100,'C'))
##ljust(),rjust()
print(aa.ljust(20,'-')); print(aa.rjust(20,'<'));print(aa.zfill(10))
##구성 함수
print("isdigit()-->",'1234'.isdigit()); print("isalpha()-->","abcd".isalpha())
print("isalnum()-->","abs123".isalnum());print("islower()-->","absdf".islower())
print("isupper()-->","ABSD".isupper());print("isspace()--->"," ".isspace())