def isLeapYear(y)
	if((y%100)==0):
		if((y%400)==0):
			print True
		else:
			print False
	else:
		if((y%4)==0):
			print True
		else:
			print False

isLeapYear(1234)

isLeapYear(1235)
isLeapYear(1236)
isLeapYear(1237)
isLeapYear(1230)
