##using Function
from os import stat_result


def Plus(x,y):
    result=0
    result=x+y
    return result
def Canculate(x,y,oper):
    x=int(input("Enter the number to X:"))
    oper=input("Enter the operator what you want to canculate:")
    y=int(input("Enter the number to Y:"))
    if oper=='+':
        return x+y
    elif oper=='-':
        return x-y
    elif oper=='*':
        return x*y
    elif oper=='/':
        return x/y
    elif oper=='%':
        return x%y
    else:
        print("Not Exist operator!")


if __name__=='__main__':
    print(Plus(10,20))
    a,b=0,0;op=0
    print(Canculate(a,b,op))