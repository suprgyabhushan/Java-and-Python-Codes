def queen(queue):
        if(len(queue)==0):
            return []
        if(len(queue)>100):
            l=100
        else:
            l=len(queue)
        s=1
        while(s<=l):
            pos=queue.pop(len(queue)-s)
            if(len(pos)==n):
                return pos
            for i in range(n):
                tmp=pos[:]
                if(not(conflict(i,pos))):
                    tmp.append(i)
                    queue.append(tmp)
            s+=1
        return  queen(queue)

def conflict(i,queue):
    x=0
    if(i in queue):
        return True
    for e in queue:
        if(abs(e-i)==abs(x-len(queue))):
            return True
        x+=1
    return False

n=95
q=[]
for i in range(n):
    q.append([i])
print queen(q)
