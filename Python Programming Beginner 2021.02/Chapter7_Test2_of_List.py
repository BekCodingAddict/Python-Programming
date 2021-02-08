aa=[10,20,30,40] 
for i in range (0,4):
    print("aa[%d]"% i,end=" ")
    print("aa[%d]"% i)
print(aa[1:3])## 1부터 3까지 3은 포함되지 않다
print(aa[:3])## 조음 부터 3까지 출력
print(aa[1:])## 1부터 끝깢 출력
bb=[10,20,30]; cc=[40,50,60]
bb+cc; print(bb+cc); print(aa*3)
print(aa[::2]); print(aa[::-2])
print(aa[::-1]); print(aa[::1])##-1 끝부터 조음까지 출력 1 조음부터 끝까지
##리스트 값을 변경 방법
bb=[10,20,30,40,50]; bb[1]=200; print(bb)# 그냥 값을 변경
bb[1:3]=[200,201]; print(bb) # 한번에 2 개 값 입력 3  포함 안 됨
bb[1]=[300,400]; print(bb)# 한 리스트 안에 다른 거 추가 됨

del(bb[1]); print(bb) # del(listname[number]) you can delete the velue from list by this del()function
del(bb[1:3]); print(bb)
aa=[]; print(aa);aa # deleting way of list 1
aa=[10,20,30];print(aa);aa=None; aa; print(aa)
#aa=[10,20,30]; print(aa); del(aa); aa; print(aa)
