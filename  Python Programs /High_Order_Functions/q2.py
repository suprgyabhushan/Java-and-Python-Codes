def f(g,l,init):
	ac=init
	for i in l:
		ac=g(ac,i)
	return ac

def sumarray(l):
	def add(x,y): return x+y
	return f(add,l,0)


def mularray(l):
	def mul(x,y): return x*y
	return f(mul,l,1)

def con(l):
	def split(x,y): return x+y
	return f(split,l,"")

def fullname(l):
	def join(x,y): return x+y
	return f(join,l,"")

def nonzero(l):
	def give(x,y):
		if(y==0):
			return 0
		else:
			return 1+x	
	return f(give,l,0)

a=[1,12,3]
b=["I","am","suprgya"]
print sumarray(a)
print mularray(a)
print con(b)
print fullname(b)
print sumarray(a)
print nonzero(a)
