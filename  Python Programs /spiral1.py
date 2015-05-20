def spiral(N, M):
    x,y = 0,0   
    dx, dy = 0, -1

    for dumb in xrange(N*M):
        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:  
            dx, dy = -dy, dx            # corner, change direction

        if abs(x)>N/2 or abs(y)>M/2:    # non-square
            dx, dy = -dy, dx            # change direction
            x, y = -y+dx, x+dy          # jump

        yield x, y
        x, y = x+dx, y+dy
print 'Spiral 3x3:'
for a,b in spiral(3,3):
    print (a,b),
