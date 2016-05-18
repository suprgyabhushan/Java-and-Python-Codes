def myfilter(f,l):
	return filter(f,l)

def odd(x):
	if((x%2)!=0):
		return x
	
def oddr(l):
	return myfilter(odd,l)

def even(x):
	if((x%2)==0):
		return x
	
def evenr(l):
	return myfilter(even,l)


def str1(x):
	y=x[::-1]
	if(y[:3]=="gni"):
		return x
def str1r(l):
	return myfilter(str1,l)
a=[1,2,3]
b=["string","coffee","talking"]
print oddr(a)
print evenr(a)
print str1r(b)

