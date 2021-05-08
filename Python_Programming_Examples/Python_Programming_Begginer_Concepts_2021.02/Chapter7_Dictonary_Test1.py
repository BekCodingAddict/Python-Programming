dic1={1:'A',2:'B',3:'C'};print(dic1);dic={'A':1,'B':2,'C':3}; print(dic)
data={'Number Id>>':20101256,'Name>>':'Otabek','Majority>>':'Computer Science and Enginering'}
print(data);data['Name>>']='Jaloli'; print(data); data['Phone number']='010 8007 7577'
print(data); data1={'Address>>':'Nowongu'}; print(data)
## Accesible
print(data.get('Jaloli')); print(data.keys()); print("Name is>>",data['Name>>'])# key yoq bolsa error
## List usulda tekshirish
print("List()>>",list(data.keys())); print(data.values()); print(list(data.values()))
print(data.items())##items() tuple shaklga aylantiradi
print('Name>>' in data)## dictonary ichda qiymat bolsa true bolmasa false
for i in data.keys():print("%s==>>%s"%(i,data[i]))