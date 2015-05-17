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
     

def daysinbetween():
	
	if (datef[2]<dater[2]):
		diff=((dater[2]-datef[2])-1)*365
		return diff
	
		def leapyearsinbetween():
			total=0
			for yearcount in range(datef[2]+1,dater[2]):				
				if (leap_year(yearcount)==True):
					total=total+1	
				print total

		def days1inbetween():
			total1=0 
			b=datef[1]+1
			while (b<=12):					
				
				if (b==1):
					total1=total1+e
					b=b+1
				if ((b==2) and (leap_year(datef[2])==True)):
					total1=total1+c
					b=b+1
				elif (b==2):					
					total1=total1+d
					b=b+1
				if (b==3):
					total1=total1+e
					b=b+1
				if (b==4):
					total1=total1+f
					b=b+1
				if (b==5):
					total1=total1+e
					b=b+1
				if (b==6):
					total1=total1+f
					b=b+1
				if (b==7):
					total1=total1+e
					b=b+1
				if (b==8):
					total1=total1+e
					b=b+1
				if (b==9):
					total1=total1+f
					b=b+1
				if (b==10):
					total1=total1+e
					b=b+1
				if (b==11):
					total1=total1+f
					b=b+1
				if (b==12):
					total1=total1+e			
					b=b+1
						
			print total1	

		def days2inbetween():
			total2=0 
			g=dater[1]-1
			while (g>=1):				
				if ((g==2) and (leap_year(dater[2])==True)):
					total2=total2+c
					g=g-1
				elif (g==2):					
					total2=total2+d
					g=g-1
				if (g==1):
					total2=total2+e
					g=g-1
				if (g==3):
					total2=total2+e
					g=g-1
				if (g==4):
					total2=total2+f
					g=g-1
				if (g==5):
					total2=total2+e
					g=g-1
				if (g==6):
					total2=total2+f
					g=g-1
				if (g==7):
					total2=total2+e
					g=g-1
				if (g==8):
					total2=total2+e
					g=g-1
				if (g==9):
					total2=total2+f
					g=g-1
				if (g==10):
					total2=total2+e
					g=g-1
				if (g==11):
					total2=total2+f
					g=g-1
				if (g==12):
					total2=total2+e
					g=g-1
			print total2

		def days3inbetween():				
			if (datef[1]==1 or datef[1]==3 or datef[1]==5 or datef[1]==7 or datef[1]==8 or datef[1]==10 or datef[1]==12):
				j=31-datef[0]
			if (datef[1]==4 or datef[1]==6 or datef[1]==9 or datef[1]==11):
				j=30-datef[0]		
			if (datef[1]==2 and leap_year(datef[2])):
				j=28-datef[0]		
			elif (datef[1]==2):
				j=29-datef[0]
			print j

		k = diff + leapyearsinbetween() + days1inbetween() + days2inbetween() + days3inbetween() + dater[0]-1	
		print k
		o=k%7
		print getweekday(o)


daysinbetween()
