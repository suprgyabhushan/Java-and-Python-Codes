def daysinbetween2():
	if (leap_year(datef[2])==False):
		if ((month==2) and (day==29)):
			print "invalid input"	
	if (datef[2]>dater[2]):
		
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
					b=b+1
				if ((b==2) and (leap_year(dater[2])==True)):
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
						
			return total1	

		def days2inbetween():
			total2=0 
			g=datef[1]-1
			while (g>=1):				
				if ((g==2) and (leap_year(datef[2])==True)):
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
			return total2

		def days3inbetween():				
			if (dater[1]==1 or dater[1]==3 or dater[1]==5 or dater[1]==7 or dater[1]==8 or dater[1]==10 or dater[1]==12):
				j=31-dater[0]
			if (dater[1]==4 or dater[1]==6 or dater[1]==9 or dater[1]==11):
				j=30-dater[0]		
			if (dater[1]==2 and leap_year(dater[2])):
				j=29-dater[0]		
			elif (dater[1]==2):
				j=28-dater[0]
			return j

		t = difference() + leapyearsinbetween() + days1inbetween() + days2inbetween() + days3inbetween() + datef[0]
		print t
		s=t%7
		print getweekday1(s)


