global bit
bit=[]



def findbit(n):
	while(n>0):
		a=n%2
		bit.append(a)
		n=n/2
	c=bit[::-1] 
	return c


def perm(n, i):
    	if i == len(n) - 1:
        	print n
    	else:
        	for j in range(i, len(n)):
            		n[i], n[j] = n[j], n[i]
            		perm(n, i + 1)
            		n[i], n[j] = n[j], n[i]
	return n	
d=findbit(3)er
print perm(d,0)







																
