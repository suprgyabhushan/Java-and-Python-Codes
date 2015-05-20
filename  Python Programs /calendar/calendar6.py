day=input("Please enter the day:")
month =input("Please enter the month: ")
year=input("Please enter the year: ")


datef=[]
datef.append(day)
datef.append(month)
datef.append(year)
print datef

dater=[31,8,2014]
list2 = [31,30]
list3 = [28,29]

c=list3[1]
d=list3[0]
e=list2[0]
f=list2[1]	

def leap_year(y):
    if (((y % 400 == 0) and (y % 100 == 0)) or ((y % 100 != 0) and (y % 4 == 0))):
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


def getweekday1(w):
	if w==0:
		return "Sunday"
	if w==1:
		return "Monday" 	
	if w==2:
		return "Tuesday"
	if w==3:
		return "Wednesday" 	
	if w==4:
		return "Thursday"
	if w==5:
		return "Friday" 	
	if w==6:
		return "Saturday"
def days3inbetween():				
	if (datef[1]==1 or datef[1]==3 or datef[1]==5 or datef[1]==7 or datef[1]==8 or datef[1]==10 or datef[1]==12):
		j=31-datef[0]
	if (datef[1]==4 or datef[1]==6 or datef[1]==9 or datef[1]==11):
		j=30-datef[0]		
	if (datef[1]==2 and leap_year(datef[2])):
		j=29-datef[0]		
	elif (datef[1]==2):
		j=28-datef[0]
	return j

def days3inbetween1():				
	if (dater[1]==1 or dater[1]==3 or dater[1]==5 or dater[1]==7 or dater[1]==8 or dater[1]==10 or dater[1]==12):
		j=31-dater[0]
	if (dater[1]==4 or dater[1]==6 or dater[1]==9 or dater[1]==11):
		j=30-dater[0]		
	if (dater[1]==2 and leap_year(dater[2])):
		j=29-dater[0]		
	elif (dater[1]==2):
		j=28-dater[0]
	return j
def daysinbetween():
	
daysinbetween()
	
	
	
