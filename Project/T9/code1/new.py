def makeleaf(t):
    return[t,[]]
def findchar(lst,ch):
    y=0
    for i in lst:
        if(i[0]==ch):
            return True,y
        y=y+1
    return False,y
def maketree(lst):
    result=['$',[]]
    for w in lst:
        t=result[1]
        for i in w:
            check,y=findchar(t,i)
            if(check==True):
                t=t[y][1]
            else:
                t.append(makeleaf(i))
    return result            
print maketree(['char','chef'])
