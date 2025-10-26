import sys
import ctypes
a=[1,2,3]
print(sys.getrefcount(a)) 
#Suppose this prints `2`.
#Why 2 and not 1?
#Because:
#- `a` is one reference
#- `getrefcount()` temporarily creates another reference when passing `a` to the function
b=a
print(sys.getrefcount(a)) #Now this prints `3`.
del b
print(sys.getrefcount(a)) #Now this prints `2`.
a=None
print(sys.getrefcount(a)) #Now this prints `1`.

def ref_count(address:int):
	return ctypes.c_long.from_address(address).value

a=[1,2,3]
print(ref_count(id(a)))
b=a
print(ref_count(id(a)))
c=a
print(ref_count(id(a)))
c=10
print(ref_count(id(a)))
b=None	
print(ref_count(id(a)))
a_id=id(a)
a=None
print(ref_count(a_id))