day=input("please day:")
month =input("Please enter the month: ")
year=input("Please enter the year: ")

datef=[]
datef.append(day)
datef.append(month)
datef.append(year)
print datef

dater=[31,8,2014]



#define a dictionary and the month is key which value is days 
  

list2 = [31,30]
list3 = [28,29]

c=list3[1]
d=list3[0]
e=list2[0]
f=list2[1]	

def leap_year(y):
    if (y % 4 == 0):
        return True
    else:
        return False

def leapyear(): 
   
      	if (leap_year(datef[2])==True):     
   	       	return  "leap year"
	else:	       	 
     		return "not a leap year"

def getweekday(w):
	if w==6:
		return "Sunday"
	if w==5:
		return "Monday" 	
	if w==4:
		return "Tuesday"
	if w==3:
		return "Wednesday" 	
	if w==2:
		return "Thursday"
	if w==1:
		return "Friday" 	
	if w==0:
		return "Saturday"
def days1inbetween1():
	total3=0 
	m=datef[1]+1
	while (m<=(dater[1]-1)):					
		
		if (m==1):
			total3=total3+e
			
		if ((m==2) and (leap_year(datef[2])==True)):
			total3=total3+c
			
		elif (m==2):					
			total3=total3+d
			
		if (m==3):
			total3=total3+e
			
		if (m==4):
			total3=total3+f
			
		if (m==5):
			total3=total3+e
			
		if (m==6):
			total3=total3+f
			
		if (m==7):
			total3=total3+e
			
		if (m==8):
			total3=total3+e
			
		if (m==9):
			total3=total3+f
			
		if (m==10):
			total3=total3+e
			
		if (m==11):
			total3=total3+f
			
		if (m==12):
			total3=total3+e
		m=m+1						
	return total3	


def days3inbetween1():				
	if (datef[1]==1 or datef[1]==3 or datef[1]==5 or datef[1]==7 or datef[1]==8 or datef[1]==10 or datef[1]==12):
		n=31-datef[0]
	if (datef[1]==4 or datef[1]==6 or datef[1]==9 or datef[1]==11):
		n=30-datef[0]		
	if (datef[1]==2 and leap_year(datef[2])):
		n=28-datef[0]		
	elif (datef[1]==2):
		n=29-datef[0]
	return n

l = days1inbetween1() + days3inbetween1() + dater[0]-1	
print l
q=l%7
print getweekday(q)


     
