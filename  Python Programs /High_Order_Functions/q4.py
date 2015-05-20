def f(x):
	def g(y):
		return y*x
	return g
list=f(2)
print list(3)
