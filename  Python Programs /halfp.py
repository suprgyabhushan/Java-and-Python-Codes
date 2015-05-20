n=input("lines")

i=1
for k in range(1,n+1):
	for j in range(i,i+k):		
		print j,
	i=i+k
	print ""
