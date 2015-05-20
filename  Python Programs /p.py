x=input("nu")
if x < 2:
 print "False"

for i in range(2, int(x ** 0.5) + 1):
 if x % i == 0:
       	print " False"
 else:
        print "True"
