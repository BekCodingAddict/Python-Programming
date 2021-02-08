mySet1={1,2,2,1,3,4,4,4,5};print(mySet1);mySet2={'Apple','Apple','Banana','Banana','Painapple'}
print(mySet2);myset3={5,4,6,7}
print(mySet1&myset3); print(mySet1.intersection(myset3))# ikkala setdagi bir xil qiymatlari aniqlab beradi
print(mySet1|myset3); print(mySet1.union(myset3))# Ikkala Set()larni birlashtiradi
print(mySet1-myset3);print(mySet1.difference(myset3))# Birinchi set()da bolib ikkinchi setda mavjud bolmagan qiymani aniqlab beradi
print(mySet1^myset3);print(mySet1.symmetric_difference(myset3))# Ozoro bir birda mavjud bolmagan  set()ni qiymatni aniqlash
##Comprehension
numList=[]
for num in range (1,6):
    numList.append(num)
print(numList); del(numList)
numList=[num for num in range(1,6)]; print("Comperhension>>%s"%numList);del(numList)
numList=[num for num in range(1,21)if num%3==0];print(numList)