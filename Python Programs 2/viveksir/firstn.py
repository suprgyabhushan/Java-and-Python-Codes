def sum_of_int(n):
	if(n<=1):
		return n
	else:
		return n+sum_of_int(n-1)

print sum_of_int(4)
