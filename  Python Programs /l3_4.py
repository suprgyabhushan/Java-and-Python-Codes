l1=[1,2,3,4,5,6,7,8,6]
l2=[1,1,2,3,6,4,8]
result=[]
for i in l1:
    for j in l2:
        if(i==j):
            result.append(j)
print result
