l=range(1,80001)
v=input("")
l.sort()
n=len(l)-1
n=n/2
m=0
if(l[0]==v):
    print True
else:
    while(n!=0 and n<len(l)):
        if(l[n]==v):
            print True
            break
        elif(l[n]<v):
            n=(len(l)+n)/2
            m=n
        else:
            n=(n+m)/2
if(n==0 or n>=len(l)):
    print False
        
        
