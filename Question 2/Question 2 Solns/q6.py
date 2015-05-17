def sumsquare(x,y):
	return (x**2)+(y**2)

def greaterEven(l):
	a=filter(lambda x:x%2==0,l)
	b=filter(lambda x:x%2!=0,l)
	c=reduce(sumsquare,a,0)
	d=reduce(sumsquare,b,0)
	if(c>d):
		return True
	else:
		return False

a=[1,2,3,4,5,6]
print greaterEven(a)
