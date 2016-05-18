a = "1110"
b = "101"
c = "0b"
work = [[],[]]

work[0] = [int(i) for i in a]
work[1] = [int(i) for i in b]

if len(work[0]) > len(work[1]):
    short = 1
    longer = 0
else:
    short = 0
    longer = 1


for i in range(1,len(work[short])+1):
        work[longer][-i] = work[longer][-i] + work[short][-i]
        if work[longer][-i] != 1:
            work[longer][-i] = 0

for i in work[longer]:
    c += str(i)

print (c)
