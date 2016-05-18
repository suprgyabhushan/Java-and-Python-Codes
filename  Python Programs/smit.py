list=[]
a=input("enter")
b=input("enter")
i=1
while (i<=a):
	d=[]
	list.append(d)
	i=i+1
j=1
while (j<=b):
	list[0].append(0)
	j=j+1
k=1
while (k<a):
	s=0		
	while (s<((k*(b-1))+1)):
	
		list[k].append(s)
		s=s+k
	k=k+1

print list

