##Function agar global variable va local variable ismi bir xil bolsa 
##Avvalo local variable qiymati boycha programma ishlaydi 
##local variable yoq bolsa 2 chi orina global variable
def Func1():
    global a; a=10
    print("func1() inside a variable's value=%d"%a)
def Func2():
    ##a=10
    print("func1() inside a variable's value=%d"%a)

a=20

Func1();Func2()