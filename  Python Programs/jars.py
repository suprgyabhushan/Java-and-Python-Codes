import tree as T

tree={}

#finally getting the buckets if they are already arranged
def ideal(lst,vol):
    count=0
    v=0
    for e in lst:
        if(e is not 0):
            v=e
            count+=1
    if((count==1) and v==vol):
        return True
    else:
        return False

#emptying the jars then transferring it and then again filling it....If in a 4 Litre bucket , in which 2 Litre is already we are filling 3 Litre Bucket  
def jars(vols,find):
    def empty(contents,i):
        new=contents[:]
        new[i]=0
        return new

    def transfer(contents,i,j):
        new=contents[:]
        new[j]+=new[i]
        new[i]=0
        if(new[j]>vols[j]):
            x=new[j]-vols[j]
            new[j]=vols[j]
            new[i]+=x
        return new

    def fill(contents,i):
        new=contents[:]
        new[i]=vols[i]
        return new
#making the whole buckets of zero content
    queue=[]
    contents=vols[:]
    for i in range(0,len(contents)):
        contents[i]=0
#should not repeat a process    
    queue=[contents]
    check=[]
    check.extend(queue)
    def process(queue,g,l):
        ex=[]
        for i in range(0,len(l)):
            x=g(l,i)
            if(not(x in check) and not(x in ex)):
                ex.append(x)
        return ex
    
    def recur(queue):
        if(len(queue)==0):
            return
        tmp=queue[0]
        for i in queue:
            if(ideal(i,find)):
                return i
        tree[str(tmp)]=[]
        l=process(queue,empty,tmp)
        tree[str(tmp)].extend(l)
        queue.extend(l)
        check.extend(l)
        l=process(queue,fill,tmp)
        tree[str(tmp)].extend(l)
        queue.extend(l)
        check.extend(l)
        l=[]
        for i in range(0,len(tmp)):
            for j in range(0,len(tmp)):
                if(i!=j):
                    a=transfer(tmp,i,j)
                    if(not(a in check)):
                        l.append(a)
        tree[str(tmp)].extend(l)
        queue.extend(l)
        check.extend(l)
        queue.pop(0)
        return recur(queue)
    return recur(queue)

def getTree(vol):
    ans=[]
    for e in tree:
        for i in tree[e]:
            if(i==vol):
                ans.append(e)
    def check(v):   
        r=0
        for e in tree:
            for i in tree[e]:
                if(str(i)==v):
                    r=str(e)
                    ans.append(e)
        if(r!=0):
            check(r)
        else:
            return
    check(ans[0])
    ans.reverse()
    return ans

f=jars([15,15,17],11)
if(f is not None):
    steps=getTree(f)
    steps.append(f)
    for e in steps:
        print e
else:
    print []
