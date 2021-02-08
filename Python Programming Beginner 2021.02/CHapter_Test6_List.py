aa=[]
for i in range(0,5):
    aa.append(i+1)
print(aa)
print(aa[::-1]);print(aa[::2])
aa[1:2]=[200,300]; print(aa); del(aa[1:3]); print(aa)
aa=[]; print(aa); aa=[10,20,30];print(aa);aa=None; print(aa)
aa=[10,20,30,40]; print(aa); aa.append(50); print(aa)
aa.pop();print(aa);aa.reverse();print(aa); aa.sort(); print(aa)
aa.insert(4,50); print(aa);aa.remove(50); print(aa);bb=[50,60]
aa.extend(bb);print(aa); aa.count(50); print(aa.count(50))
aa.clear();aa=bb.copy(); print(aa); bb=sorted(aa);print(aa)
