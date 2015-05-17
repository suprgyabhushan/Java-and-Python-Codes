def mymap(f,l):
	return map(f,l)

def dbl(x):
	return x*2
def dblarray(l):
	return mymap(dbl,l)
def add(x):
	return x+2
def add2array(l):
	return mymap(add,l)

def str1(x):
	return len(x)
def strlenarray(l):
	return mymap(str1,l)

a=[1,2,3]
b=["I","am","Suprgya"]
print dblarray(a)
print add2array(a)
print strlenarray(b)
	
