l=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result=[]
i=0
n=len(l[0])
while(i<n):
	row=[]
	for x in l:
		row.append(x[i])
	result.append(row)
	i=i+1
print result
