class animal:
	def __init__(self,x):
		self.animal=x
	@property
	def speak(self):
		if(self.animal=="Lion"):
			return "Roar"
		if(self.animal=="goat"):
			return "Meh"
		

if __name__=="__main__":
	lion=animal("Lion")	
	print lion.speak

	
