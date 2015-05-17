rows=input("no")
for num in xrange(rows):
	print(''.join("1" * min(num+1,rows-num)).center(rows))
