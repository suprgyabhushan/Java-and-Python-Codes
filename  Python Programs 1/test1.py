n=input("enter number:")
d=n
i="y"
while(i=="y"):
    n=input("enter number:")
    if(n>=d):
        d=n
    print d
    i= raw_input("y-continue or n-exit:")
