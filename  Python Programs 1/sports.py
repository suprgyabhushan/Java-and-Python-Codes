a={"A":["S1","S2","S3"],"B":["S2","S4"],"C":["S3"],"D":["S1","S4","S5"]}
def invert(b):
    result={}
    for key in b:
        for s in b[key]:
            if(s in result):
                result[s].append(key)
            else:
                result[s]=[]
                result[s].append(key)
    print result 
invert(a)
