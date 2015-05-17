#!/usr/bin/python

import string

class Dictionary:
	
	global _end #defining the global name _end
	_end="$" #initialise the _end value as $
	
	def __init__(self, fileName):
		self.words=[]
		self.root=dict()
		fin = open(fileName, 'r')
		while(True): #creating a list of words
			line = fin.readline()
			if(line == ''):
				break
			else:
				self.words.append(string.strip(line))
				
		for word in self.words: #creating dictionary of dictionaries of words in a file
			current_dict=self.root			
			for letter in word:
				current_dict=current_dict.setdefault(letter,{})
			current_dict=current_dict.setdefault(_end,{})
	def printsuffix(self): # printing suffix tree
		current_dict=self.root
		return current_dict
			
	def findPrefix(self, word): # finding prefix
		current_dict=self.root
		
		a=0
		for letter in word:
			if letter in current_dict:
				current_dict = current_dict[letter]
			else:
				a=1
		if(a==0):
			return True
		elif(a==1):
			return False


if __name__ == "__main__":
	dictionary=Dictionary("linux.words.txt")
	print dictionary.printsuffix()
	def t1():
		print dictionary.findPrefix("sup")
		print dictionary.findPrefix("fdaygskhksdhlijjoouuyysxuitau")
		print dictionary.findPrefix("anshu")
	t1()
	

