n=input("no. of numbers to be added:")
i=1
b=[]
sum=0
while(i<=n):
    a= input("enter number "+str(i)+":")
    b.append(a)
    sum=sum+a
    i=i+1
print b
print "total is "+str(sum)

