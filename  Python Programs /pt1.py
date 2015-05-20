def c(n,k):
	if((k<0) or (k>n)):
		return 0
	elif((k==0) or (n==0)):
		return 1
	else:
		return c(n-1,k-1) + c(n-1,k)

global i
i=[]

def p(top,l):	
	if(l<=top):
		a=c(top,l)					
		i.append(a)		
		p(top,l+1)
		return i
	
def Triangle(line):
	return p(line-1,0)	

print Triangle(4)	
