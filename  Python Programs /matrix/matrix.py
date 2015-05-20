import random
rows=input("e")
collumns=input("f")
random_matrix = [[random.random for j in range(collumns)] for i in range(rows)]
for i in range(rows):
    print random_matrix[i]


