family = [
    {'name': 'Suraj', 'parent': ''},
    {'name': 'Jai', 'parent': 'Suraj'},
    {'name': 'Medha', 'parent': 'Jai'},
    {'name': 'Paresh', 'parent': 'Jai'},
    {'name': 'Manju', 'parent': 'Suraj'},
    {'name': 'Vimmi', 'parent': 'Manju'},
    {'name': 'Nimmi', 'parent': 'Manju'},
   
]


list0=family[0].values()
def AreSiblings(a,b):
	global c
	c=[]
	global d
	d=[]
	if (a in list0) :
		return "No Sibling can exist"
	if (b in list0) :
		return "No Sibling can exist"
	
	for i in range(1,7):
		
		if (family[i].values()[0]==a):
			
			c=family[i].values()
	s=c[1]		
		
	for j in range(1,7):
		
		if (family[j].values()[0]==b):
			
			d=family[j].values()
	t=d[1]

	if(s==t):
		return True
	else:
		return False

def isDescendant(a,b):
	
	if (a in list0)  :
		return "No Descendant exist"
		
	
	else:
	
		for i in range(1,7):		
			if (family[i].values()[0]==a):			
				k=family[i].values()
				a=k[1]
				print a,
				if(a==b):
					print True
				else:
					isDescendant(a,b)
	
	
def AreCousins(a,b):
	global g
	g=[]
	global h
	h=[]
	if ((a in list0) or (b in list0)) :
		return "No Cousin exist"
	elif(AreSiblings(a,b)==True):
		return "Not Cousins"
	else:
	
		for i in range(1,7):
			if (family[i].values()[0]==b):
				g=family[i].values()
		x=g[1]		
		
		for j in range(1,7):
			if (family[j].values()[0]==a):
				h=family[j].values()
		y=h[1]
	
		if(AreSiblings(x,y)==True):
			return True
		else:
			return False

def AllDescendants(b):
	for i in range(1,7):		
		if (family[i].values()[1]==b):			
			c=family[i].values()
			m=c[0]
			print m,
			AllDescendants(m)
				
		
	
def AllAncestors(b):	
	for i in range(1,7):		
		if (family[i].values()[0]==b):			
			c=family[i].values()
			m=c[1]
			print m,
			AllAncestors(m)


def CommonClosestAncestor(a,b):
	
	if((a in list0) or (b in list0)):
		print "Suraj"
	else :

	
		global n
		n = []
		global m
		m = []
		for i in range(1,7):
			if (family[i].values()[0]==a):
				c=family[i].values()
				m=c[1]

		for j in range(1,7):
			if (family[j].values()[0]==b):
				d=family[i].values()
				n=d[1]
		if(m==n):
			print m
		else:
			CommonClosestAncestor(m,n)
						
e="Medha"
f="Suraj"

AllDescendants(f)
print ""
AllAncestors(e)
print ""
CommonClosestAncestor(e,f)

print AreSiblings(e,f)
print AreCousins(e,f)

isDescendant(e,f)

