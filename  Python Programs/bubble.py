def bubble(l):
	n=len(l)
	for i in range(l):
		t=0
		if(l[i]>l[i+1]):
			temp=l[i]
			l[i]=l[i+1]
			l[i+1]=temp
		else:
			t=t+1
		if(t==n-1):
			break
		print temp
a=[1,2,3]
bubble(a)
						
