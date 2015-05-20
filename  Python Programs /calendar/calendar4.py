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
          



def daysinbetween2():	
	if (leap_year(datef[2])==False):
		if ((month==2) and (day==29)):
			print "invalid input"	
		
	elif ((datef[2]==dater[2]) and (datef[1]>dater[1])):
	
		def days1inbetween1():
	
			total3=0 
			m=dater[1]+1
			while (m<(datef[1])):					
		
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
			if (dater[1]==1 or dater[1]==3 or dater[1]==5 or dater[1]==7 or dater[1]==8 or dater[1]==10 or dater[1]==12):
				n=31-dater[0]
			if (dater[1]==4 or dater[1]==6 or dater[1]==9 or dater[1]==11):
				n=30-dater[0]		
			if (dater[1]==2 and leap_year(dater[2])):
				n=29-dater[0]		
			elif (dater[1]==2):
				n=28-dater[0]
			return n
		y = days1inbetween1() + days3inbetween1() + datef[0]	
		print y
		z=y%7
		print getweekday1(z)


daysinbetween2()
print days1inbetween1()
print days3inbetween1()

