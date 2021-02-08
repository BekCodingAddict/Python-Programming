print(">>%d"%100)
print("%d/%d=%d"%(200,100,0.5))
print("%d/%d=%f"%(200,100,0.5))
print("%10d"%123)
print("%10.4f"%123.45) ##10 daraja surib noldan keyin 4 ta songacha print

#string
print("%s"%"Python is easy!")
print("%50s"%"Python is very easy") ##Matin yuqaridagiga kora siljiganini korish mumkin

print("{0:d} {1:5d} {2:05d}".format(123,123,123))
print("{2:d} {1:d} {0:d}".format(100,200,300))#farmatdan foydalanib printichidagilarni tartiblash

print("Bir qator. Va yana bir qator!")
print("Bir qator.\n Va yana bir qator!") ## \n qoshimchasi qator almashtrish

print(bin(11))##2진수
print(oct(11))##8진수
print(hex(11))##16 진수

a=123
print(type(a)) ##automatic declation

a=(100==100) ##Bool using mathod
b=(10>100) 
print(a,b)