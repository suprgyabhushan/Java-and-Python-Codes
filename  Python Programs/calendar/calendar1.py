day=input("please day:")
month =input("Please enter the month: ")
year=input("Please enter the year: ")

datef=[]
datef.append(day)
datef.append(month)
datef.append(year)
print datef

dater=[7,12,2014]

#define a dictionary and the month is key which value is days 
  
list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
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



def leapyearsinbetween():
	total=0
	if (datef[2]==dater[2]):		
		return total

def days1inbetween():
	total1=0 
	b=datef[1]+1
	while (b<=(dater[1]-1)):					
		
		if (b==1):
			total1=total1+e
			
		if ((b==2) and (leap_year(datef[2])==True)):
			total1=total1+c
			
		elif (b==2):					
			total1=total1+d
			
		if (b==3):
			total1=total1+e
			
		if (b==4):
			total1=total1+f
			
		if (b==5):
			total1=total1+e
			
		if (b==6):
			total1=total1+f
			
		if (b==7):
			total1=total1+e
			
		if (b==8):
			total1=total1+e
			
		if (b==9):
			total1=total1+f
			
		if (b==10):
			total1=total1+e
			
		if (b==11):
			total1=total1+f
			
		if (b==12):
			total1=total1+e
		b=b+1						
	return total1	


def days3inbetween():				
	if (datef[1]==1 or datef[1]==3 or datef[1]==5 or datef[1]==7 or datef[1]==8 or datef[1]==10 or datef[1]==12):
		j=31-datef[0]
	if (datef[1]==4 or datef[1]==6 or datef[1]==9 or datef[1]==11):
		j=30-datef[0]		
	if (datef[1]==2 and leap_year(datef[2])):
		j=28-datef[0]		
	elif (datef[1]==2):
		j=29-datef[0]
	return j

	
k = days1inbetween() + days3inbetween() + dater[0]-1

l=k%7
def getweekday(m):
	if l==6:
		return "Sunday"
	if l==5:
		return "Monday" 	
	if l==4:
		return "Tuesday"
	if l==3:
		return "Wednesday" 	
	if l==2:
		return "Thursday"
	if l==1:
		return "Friday" 	
	if l==0:
		return "Saturday"	 	




		
  
 
print leapyear() 
print leapyearsinbetween()
print days1inbetween()
print days3inbetween()
print k
print l
print getweekday(l)






     
