def pallin(b):
    i= len(b)-1
    result=""
    
    while(i>=0):
        a=b[i]
        result = result + a
        i=i-1
    return result

x= raw_input("enter:")
print pallin(x)
