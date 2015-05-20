n=input("enter the no of lines")
v=n
str1=""#space
b=1#initializer
while(b!=0):
	i=b
	x=1
	while(x!=0):
		str1=str1+str(x)
		if(x<i):
			x=x+1
		else:
			x=x-1
			i=i-1
	if(b<n):
		b=b+1
	else:
		b=b-1
		n=n-1
	print str1.center(v*2)
	str1=""
