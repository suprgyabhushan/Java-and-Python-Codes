def hanoi(ndisks, startPeg, endPeg):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg)
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
 
hanoi(5,1,3)
