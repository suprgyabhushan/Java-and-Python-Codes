def num():
	n=input("enter a number")
	i=1
	sum=0
	a=[]
	while i<=n:
		x=input("enter a no" + str(i) + ":")
		a.append(x)
		sum=sum+i
		i+=1
	a.reverse()
	print " array" + str(a)
	print
	print
	print "sum" + str(sum)
num()
