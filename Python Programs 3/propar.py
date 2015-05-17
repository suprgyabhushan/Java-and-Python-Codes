class Rectangle:
	def __init__(self,l,b):
		self.breadth=b
		self.length=l
	@property
	def area(self):
		return self.length*self.breadth

if __name__=="__main__":
	r=Rectangle(1,2)
	print r.area

