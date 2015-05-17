lst="abc"
n1=input("enter n1")
n2=input("enter n2")
n3=input("enter n3")
class Per(str):
	def __init__(self,a):
		self=a	
	def append(self,a):
		self+a

def findper(result,na,nb,nc):
	result1=[]
	result2=[]
	result3=[]
	result1=result[:]
	result2=result[:]
	result3=result[:]
	y=0
	for i in lst:	
		if(na!=0 and i=='a'):
			result1.append('a')
			na=na-1
			y=1
			findper(result1,na,nb,nc)
			if(na==0 and nb==0 and nc==0):
				print result1
		if(y==1):
			na=na+1
			y=0
		if(nb!=0 and i=='b'):
			result2.append('b')
			nb=nb-1
			y=1
			findper(result2,na,nb,nc)
			if(na==0 and nb==0 and nc==0):
				print result2
		if(y==1):
			nb=nb+1
			y=0
		if(nc!=0 and i=='c'):
			result3.append('c')
			nc=nc-1
			findper(result3,na,nb,nc)
			if(na==0 and nb==0 and nc==0):
				print result3
findper([],n1,n2,n3)
