l1=[[1,2],[3,4],5]
result=[] 
result2=[]
for i in l1:
    if(type(i)==list):
        for j in i:
            result2.insert(0,j)
        result.insert(0,result2)
        result2=[]
    else:
        result.insert(0,i)
print result
