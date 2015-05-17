den=input("enter the list : ")
total=input("enter the total : ")
solution=[]
new=[]
result=[]
for b in den:
	total1=total-b
	if((total>total1) or (total1!=0)):
		solution.append(b)
print solution

def first_algo(lis):			
	
	while(sum(new)!=total):
		for b in range(0,len(lis)):
			total1=total-solution[0]
			total2=total1-lis[b]	
			if(total2==0):
				solution.append([solution[0],lis[b]])
				new.append([solution[0],lis[b]])
				
				print new[0]
			elif(total>total2):
				solution.append([solution[0],lis[b]])
			elif(total2<0):
				solution.append([solution[0],lis[b]])
				c=solution.index([solution[0],lis[b]])
				solution.pop(c)
	
		solution.pop(0)	
		print solution
		print solution[0]


	while(sum(new)!=total):
		for b in range(0,len(lis)):
			total1=total-sum(solution[0])
			total2=total1-sum(lis[b])	
			if(total2==0):
				solution.append([solution[0],lis[b]])
				new.append([solution[0],lis[b]])
				
				print new[0]
			elif(total>total2):
				solution.append([solution[0],lis[b]])
			elif(total2<0):
				solution.append([solution[0],lis[b]])
				c=solution.index([solution[0],lis[b]])
				solution.pop(c)
		
		solution.pop(0)	
		print solution
		print solution[0]



		
first_algo(den)	
