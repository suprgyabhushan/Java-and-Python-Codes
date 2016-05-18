def makeChange(Q,D):
	
	level={Q:0}
	parent={Q:None}
	i=1
	frontier=[Q]
	next=[]
	while(frontier):
		
		for u in frontier:
			for v in D[u]:
				if v not in level:
					level[v]=i
					parent[v]=u
					next.append(v)
		frontier=next
		i+=1
	return frontier

S=10
L=[1,2,3]
print makeChange(S,L)

