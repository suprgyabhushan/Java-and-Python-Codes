day=input("Please enter the date:")
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

def daysinbetween():
	if (leap_year(datef[2])==False):
		if ((month==2) and (day==29)):
			print "invalid input"	
	
	elif (datef[2]<dater[2]):
		print "Your Date is earlier than Reference Date"
		
		def difference():
			diff=((dater[2]-datef[2])-1)*365
			return diff
	
		def leapyearsinbetween():
			total=0
			for yearcount in range(datef[2]+1,dater[2]):				
				if (leap_year(yearcount)==True):
					total=total+1	
			return total

		def days1inbetween():
			total1=0 
			b=datef[1]+1
			while (b<=12):					
				
				if (b==1) or (b==3) or (b==5) or (b==7) or (b==8) or (b==10) or (b==12):
					total1=total1+e					
				if ((b==2) and (leap_year(datef[2])==True)):
					total1=total1+c					
				elif (b==2):					
					total1=total1+d					
									
				if (b==4) or (b==6) or (b==9) or (b==11):
					total1=total1+f	
				b=b+1
			return total1	

		def days2inbetween():
			total2=0 
			g=dater[1]-1
			while (g>=1):				
				if ((g==2) and (leap_year(dater[2])==True)):
					total2=total2+c					
				elif (g==2):					
					total2=total2+d					
				if (g==1) or (g==3) or (g==5) or (g==7) or (g==8) or (g==10) or (g==12):
					total2=total2+e					
								
				if (g==4) or (g==6) or (g==9) or (g==11):
					total2=total2+f		
				
				g=g-1	
			return total2		
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
		k = difference() + leapyearsinbetween() + days1inbetween() + days2inbetween() + days3inbetween() + dater[0]-1	
		print k
		o=k%7
		print getweekday(o)

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
				
				if (b==1) or (b==3) or (b==5) or (b==7) or (b==8) or (b==10) or (b==12):
					total1=total1+e					
				if ((b==2) and (leap_year(dater[2])==True)):
					total1=total1+c					
				elif (b==2):					
					total1=total1+d					
									
				if (b==4) or (b==6) or (b==9) or (b==11):
					total1=total1+f					
									
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
				if (g==1) or (g==3) or (g==5) or (g==7) or (g==8) or (g==10) or (g==12):
					total2=total2+e					
								
				if (g==4) or (g==6) or (g==9) or (g==11):
					total2=total2+f					
				
				g=g-1	
			return total2
		
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

		t = difference() + leapyearsinbetween() + days1inbetween() + days2inbetween() + days3inbetween1() + datef[0]
		print t
		s=t%7
		print getweekday1(s)


	
	
	if ((datef[2]==dater[2]) and (datef[1]<dater[1])):
		print "Your Date is earlier than Reference Date"
	
		def days1inbetween1():
			total3=0 
			m=datef[1]+1
			while (m<=(dater[1]-1)):					
				if ((m==1) or (m==3) or (m==5) or (m==7) or (m==8) or (m==10) or (m==12)):
					total3=total3+e				
				if ((m==2) and (leap_year(datef[2])==True)):
					total3=total3+c				
				elif (m==2):					
					total3=total3+d			
				if (m==4) or (m==6) or (m==9) or (m==11):
					total3=total3+e			
				
				
				m=m+1						
			return total3	
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

		
		l = days1inbetween1() + days3inbetween() + dater[0]-1
		print l	
		q=l%7
		print getweekday(q)



	elif ((datef[2]==dater[2]) and (datef[1]>dater[1])):
		print "Your Date is later than Reference Date"		
		def days1inbetween1():	
			total3=0 
			m=dater[1]+1
			while (m<=(datef[1]-1)):					
		
				if ((m==1) or (m==3) or (m==5) or (m==7) or (m==8) or (m==10) or (m==12)):
					total3=total3+e				
				if ((m==2) and (leap_year(dater[2])==True)):
					total3=total3+c				
				elif (m==2):					
					total3=total3+d			
				if (m==4) or (m==6) or (m==9) or (m==11):
					total3=total3+e			
				
				m=m+1										
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
		return total3
		y = days1inbetween1() + days3inbetween1() + datef[0]
		print y	
		z=y%7
		print getweekday1(z)


	if ((datef[2]==dater[2]) and (datef[1]==dater[1]) and (datef[0]<dater[0])):
		print "Your Date is earlier than Reference Date"
		
		def difference():
			diff=(dater[0]-datef[0])-1
			return diff	
		v=difference()
		print v
		x=v%7
		print getweekday(x)

'''def getnextweekday(w):
	def previousweekday(w):
		def nextDate(d) :
			def daysinmonth(m,y):'''		 

daysinbetween()



