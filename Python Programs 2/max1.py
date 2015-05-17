number=int(raw_input("Enter a number"))
max=int(raw_input("enter a number1"))
i=2
while i<=number :
	x=int(raw_input("enter a number" + str(i)))
	if x>max:
		max=x
        i=i+1
print max
        
