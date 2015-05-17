n=input("enter")
str1=""
v=n
b=1
while(b!=0):
    x=1
    i=b
    while(x!=0):
        str1=str1+str(x)
        if(x<i):
            x=x+1
        else:
            x=x-1
            i=i-1
    if(b<n):
        b=b+1
    else:
        b=b-1
        n=n-1
    print str1.center(2*v)
    str1=""

