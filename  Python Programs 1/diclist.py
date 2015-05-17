Sports=['Football','Cricket']
People=[['Nikunj','Suprgya'],['Nikunj','Smit']]
dict1=zip(Sports,People)
print dict1
dict2=dict(dict1)
print dict2
print dict2.items()
print dict2.keys()
print dict2.values()
for key in dict2:
	print key
a=dict2.get('Cricket')
print a
print a[1]
	
