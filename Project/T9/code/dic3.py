def make_suffix(words):
     root = dict()
     for word in words:
         current_dict = root
         for letter in word:	    	
             current_dict = current_dict.setdefault(letter, {})
         #current_dict = current_dict.setdefault(_end)
     return root

students=['suprgya', 'supriya', 'ishaan', 'swamita']
print make_suffix(students)

def in_suffix(suffix, word):
    current_dict = suffix
    for letter in word:
        if letter in current_dict:
             current_dict = current_dict[letter]
	     return True
        else:
             return False
    

print in_suffix(make_suffix(students), 'as')
