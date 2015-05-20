def sum(x,y):
	return x+y

def greaterEven(l):
	a=filter(lambda x:x%2==0,l)
	b=filter(lambda x:x%2!=0,l)
	c=reduce(sum,a,0)
	d=reduce(sum,b,0)
	if(c>d):
		return True
	else:
		return False

a=[1,2,3,4,5]
print greaterEven(a)
	
