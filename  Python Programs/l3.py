l1=[1,2,3,4,5,6,7,8,6]
l2=[1,1,2,3,6,4,8]
l3=[]
for i in l1:
    if((i in l2) and (i not in l3)):
        l3.append(i);
print l3
