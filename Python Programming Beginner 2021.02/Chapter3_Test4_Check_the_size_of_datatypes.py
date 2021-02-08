import sys
##번수 선언부분  
intvar,floatvar,boolvar,strvar,listvar,tuplevar,dictvar,setvar=[None]*8

#메인코드 부분
if __name__ == "__main__":
    invar=0
    floatvar=0.0
    boolvar=True
    strvar=''
    listvar=[]
    tuplevar=()
    dictvar={}
    setvar=set()

    print('size of int datatype>>',sys.getsizeof(intvar))
    print('size of float datatype>>',sys.getsizeof(floatvar))
    print('size of bool datatype>>',sys.getsizeof(boolvar))
    print('size of string datatype>>',sys.getsizeof(strvar))
    print('size of list datatype>>',sys.getsizeof(listvar))
    print('size of tuple datatype>>',sys.getsizeof(tuplevar))
    print('size of dict datatype>>',sys.getsizeof(dictvar))
    print('size of set datatype>>',sys.getsizeof(setvar))