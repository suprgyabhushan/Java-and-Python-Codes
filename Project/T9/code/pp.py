#!/usr/bin/python

import string

class Dictionary:
	def __init__(self, fileName):
    		self.words = []
    		fin = open(fileName, 'r')
    		while(True):
      			line = fin.readline()
      			if(line == ''):
        			break
      			else:
        			self.words.append(string.strip(line))

	def __str__(self):
		s = ""
		for w in self.words:
			s += w +"\n" 
			return s	
		'''root = dict()
		for word in self.words:
			current_dict = root
			for letter in word:	    	
				current_dict = current_dict.setdefault(letter, {})
  	

	def find_prefix(self, word):
		current_dict = self.root
		print current_dict
		for letter in word:
			if letter in current_dict:
				#current_dict = current_dict[letter]
				return True
			else:
				return False'''



if __name__ == "__main__":
	#students=['BACK', 'BAN', 'BAT', 'BIN','BINARY','BANTER','BRACKET','BRAG']
	dictionary = Dictionary("linux.words.txt")
	print dictionary
	#def t1():
	#	print dictionary.find_prefix("su")
	#t1()


