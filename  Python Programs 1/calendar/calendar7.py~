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

def leapyear(year):    
      	if (leap_year(year)==True):     
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



def days1inbetween(month,year):
	total1=0 
	b=month+1
	while (b<=12):				
		if (b==1):
			total1=total1+e					
		if ((b==2) and (leap_year(year)==True)):
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

def days2inbetween(month,year):
	total2=0 
	g=month-1
	while (g>=1):				
		if ((g==2) and (leap_year(year)==True)):
			total2=total2+c					
		elif (g==2):					
			total2=total2+d					
		if (g==1):
			total2=total2+e					
		if (g==3):
			total2=total2+e					
		if (g==4):
			total2=total2+f					
		if (g==5):
			total2=total2+e					
		if (g==6):
			total2=total2+f					
		if (g==7):
			total2=total2+e					
		if (g==8):
			total2=total2+e					
		if (g==9):
			total2=total2+f					
		if (g==10):
			total2=total2+e					
		if (g==11):
			total2=total2+f					
		if (g==12):
			total2=total2+e
		g=g-1	
	return total2	


def daysinbetween():

	if (leap_year(datef[2])==False):
		if ((month==2) and (day==29)):
			print "invalid input"	
	
	elif (datef[2]<dater[2]):
		print "Your Date is earlier than Reference Date"		
		def difference():
			diff=((dater[2]-datef[2])-1)*365
			return diff
		def leapyearsinbetween(year1,year2):
			total=0
			for yearcount in range(year1+1,year2):				
				if (leap_year(yearcount)==True):
					total=total+1	
			return total			
	print leapyearsinbetween(datef[2],dater[2])
	print days1inbetween(datef[1],datef[2])
	print days2inbetween(dater[1],dater[2])
		
	if (datef[2]>dater[2]):
		print "Your Date is later than Reference Date"
		
		def difference():
			diff=((datef[2]-dater[2])-1)*365
			return diff
	
		def leapyearsinbetween():
			total=0
			for yearcount in range(dater[2]+1,datef[2]):				
				if (leap_year(yearcount)==True):
					total=total+1	
			return total

		def days1inbetween():
			total1=0 
			b=dater[1]+1
			while (b<=12):					
				
				if (b==1):
					total1=total1+e					
				if ((b==2) and (leap_year(dater[2])==True)):
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

		def days2inbetween():
			total2=0 
			g=datef[1]-1
			while (g>=1):				
				if ((g==2) and (leap_year(datef[2])==True)):
					total2=total2+c					
				elif (g==2):					
					total2=total2+d					
				if (g==1):
					total2=total2+e					
				if (g==3):
					total2=total2+e					
				if (g==4):
					total2=total2+f					
				if (g==5):
					total2=total2+e					
				if (g==6):
					total2=total2+f					
				if (g==7):
					total2=total2+e					
				if (g==8):
					total2=total2+e					
				if (g==9):
					total2=total2+f					
				if (g==10):
					total2=total2+e					
				if (g==11):
					total2=total2+f					
				if (g==12):
					total2=total2+e
				g=g-1	
			return total2
		

		t = difference() + leapyearsinbetween() + days1inbetween() + days2inbetween() + days3inbetween1() + datef[0]
		s=t%7
		print getweekday1(s)


	
	
	if ((datef[2]==dater[2]) and (datef[1]<dater[1])):
		print "Your Date is earlier than Reference Date"
	
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
		
		l = days1inbetween1() + days3inbetween() + dater[0]-1	
		q=l%7
		print getweekday(q)



	elif ((datef[2]==dater[2]) and (datef[1]>dater[1])):
		print "Your Date is later than Reference Date"		
		def days1inbetween1():	
			total3=0 
			m=dater[1]+1
			while (m<=(datef[1]-1)):					
		
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
		y = days1inbetween1() + days3inbetween1() + datef[0]	
		z=y%7
		print getweekday1(z)


	if ((datef[2]==dater[2]) and (datef[1]==dater[1]) and (datef[0]<dater[0])):
		print "Your Date is earlier than Reference Date"
		
		def difference():
			diff=(dater[0]-datef[0])-1
			return diff	
		v=difference()
		x=v%7
		print getweekday(x)

'''def getnextweekday(w):
	def previousweekday(w):
		def nextDate(d) :
			def daysinmonth(m,y):'''		 

daysinbetween()



