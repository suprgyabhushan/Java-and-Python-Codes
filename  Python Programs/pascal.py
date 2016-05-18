n=input("enter a number")
def pascal(n):
    if(n==1):
        return [1]
#    elif(n==2):
#        return [1,1]
    else:
        m=[1]
        while(len(m)!=n-1):
            #a=pascal+pascal[len(m)-1]
            q=pascal(n-1)
            a=q[len(m)]+q[len(m)-1]
            m.append(a)
        m.append(1)    
        return m
x=pascal(n)
for i in x:
    print i,
