a=[4,2,3,0]
b=["I","am","Suprgya"]
c=["Suprgya","Bhushan"]
d=["string","talking","suprgya"]
print map(lambda x:x*2,a)
print map(lambda x:x+2,a)
print map(lambda x:len(x),b)

print reduce(lambda x,y:x+y,a)
print reduce(lambda x,y:x*y,a)
print reduce(lambda x,y:x+" "+y,b)
print reduce(lambda x,y:x+" "+y,c)

print reduce(lambda x,y:x+int(y!=0),a,0)


a=[4,2,3]
print filter(lambda x: x % 2 == 0,a)
print filter(lambda x: x % 2 != 0,a)
print filter(lambda x:x.endswith("ing"),d)



