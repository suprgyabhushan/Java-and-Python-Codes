def qu(l):
    r=[]
    if(l[0]==7):
        r.append(0)
    elif(l[0]==6):
        r.append(1)
    else:
        r.append(l[0]+2)
    if(l[1]==7):
        r.append(0)
    elif(l[1]==6):
        r.append(1)
    else:
        r.append(l[1]+2)
    return r
row = input("enter row:")
col = input("enter column:")
first=[]
first.append(row)
first.append(col)
result=[]o
result.append(first)
for i in range(7):
    z=qu(first)
    result.append(z)
    first=z
print result


