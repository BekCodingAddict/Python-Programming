Uzfoods=['SHorva','Osh','Manti','Chuchvara','Shashlik']
sides=['Non','Shakorob','Saryoq']
for food, side in zip(Uzfoods,sides):
    print(food,'==>',side)## Bir martada ikkta list bilan ishlash mumkin  eng kichkina list qiymatigacha boradi
TupList=list(zip(Uzfoods,sides)); print("List==>",TupList)###ikkita listni birlashtirib dictanary shaklida ishlatsa boladi
NeDict=dict(zip(Uzfoods,sides)); print("Dictonary==>>",NeDict)
Uzsides=sides;sides.append('Makaron'); print(Uzsides)## uZSIDES LISTGA MEN QIYMAT QOSHMADIM LEKIN MAKARON PRINT BOLDI
uZSIDES2=sides[:];sides.append('SPAGETTI'); print(uZSIDES2)## Spagetti print bolmadi shallow copy oldi olindi

