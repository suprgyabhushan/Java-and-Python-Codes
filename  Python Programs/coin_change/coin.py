def makeChange(Q,coins_available,coins_so_far):
	if (sum(coins_so_far)==n):
		yield coins_so_far
	elif (sum(coins_so_far)>n):
		pass
	elif (coins_available==[]):
		pass
	else:
		for c in makeChange(n,coins_available[:],coins_so_far+[coins_available[0]]):
			yield c
		for c in makeChange(n,coins_available[1:],coins_so_far):
			yield c
n=10
coins=[3,2,1]
solutions=[s for s in makeChange(n,coins,[])]
for s in solutions:
	print s
print "optimal value : ", min(solutions,key=len)

