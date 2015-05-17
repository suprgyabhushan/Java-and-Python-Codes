l=[0,0,0]
l[0]= input("enter day:")
l[1]= input("enter month(in number):")
l[2]= input("enter year:")
def isEarlier(l,r):
    if(l[2]>r[2]):
        return True
    elif (l[2]==r[2]):
        if(l[1]>r[1]):
            return True
        elif (l[1]==r[1]):
            if(l[0]>r[0]):
                return True
    else:
        return False
def nextDate(r):
    if(r[1]==1):
        m=31
    elif(r[1]==2):
        v=r[2]
        if((((v%100)==0) and ((v%400)==0)) or (((v%100)!=0) and (((v%4)==0)))):
            m=29
        else:
            m=28
    elif(r[1]==3):
        m=31
    elif(r[1]==4):
        m=30
    elif(r[1]==5):
        m=31
    elif(r[1]==6):
        m=30
    elif(r[1]==7):
        m=31
    elif(r[1]==8):
        m=31
    elif(r[1]==9):
        m=30
    elif(r[1]==10):
        m=31
    elif(r[1]==11):
        m=30
    else:
        m=31
    if(r[0]==31 and r[1] ==12):
        r[0]=1
        r[1]=1
        r[2]=r[2]+1
    else:
        if(r[0]==m):
            r[0]=1
            r[1]=r[1]+1
        else:
            r[0]=r[0]+1
    return r

def diffBetwDates(r,l):
    if(not isEarlier(r,l)):
        z=l
        l=r
        r=z
    count=0
    while(r!=l):
        count=count + 1
        r=nextDate(r)
    return count

def weekday(j):
    k=[11,9,2014]
    d= diffBetwDates(k,j)
    n= d%7
    if(n==0):
        return "Thursday"
    elif(n==1):
        return "Friday"
    elif(n==2):
        return "Saturday"
    elif(n==3):
        return "Sunday"
    elif(n==4):
        return "Monday"
    elif(n==5):
        return "Tuesday"
    elif(n==6):
        return "Wednesday"

print weekday(l)



        

