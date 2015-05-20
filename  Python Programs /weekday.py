y=[13,9,2014]
r=[11,9,2014]
ml=[29]
m=[31,28,31,30,31,30,31,31,30,31,30,31]

if (((y[2]%100)==0) and ((y[2]%400)==0)) or (((y[2]%100)==0) and ((y[2]%4)==0)):
	print "leap year"
days=(y[0]-r[0])
if (days>9):
	a=days%7
	if (a==0):
		print "Sunday"
	elif (a==1):
		print "Monday"
	elif (a==2):
		print "Tuesday"
	elif (a==3):
		print "Wednesday"
	elif (a==4):
		print "Thursday"
	elif (a==5):
		print "Friday"
	elif (a==6):
		print "Saturday"
elif (days==0):
	print "Sunday"

elif (days==1):
	print "monday"

elif (days==2):
	print "tuesday"

elif (days==3):
	print "wed"
elif (days==4):
	print "t"
elif (days==5):
	print "f"

elif (days==6):
	print "Sa"
