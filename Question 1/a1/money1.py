#!/usr/bin/python

def makeChange(Q, D):

## Helper functions - begin ######################
  # Given a partial solution s, extend it by one step using each of the denominations available in D.
  # For doing the above, create a copy of s first, and append one of the denominations to it.
  # Return the list of these extended solutions.
  def extendSolution(s):
    nss = []
    for d in D:
      ns = s[:]
      ns.append(d)
      nss.append(ns)
    return nss
  
  UNDERSHOOT = -1 # Solution adds up to less than Q
  BULLSEYE   = 0  # Solution adds up to Q, hence is a complete solution.
  OVERSHOOT  = 1  # Solution adds up to greater than Q.

  def isSolution(s):
    sum = reduce(lambda x, y : x + y, s, 0)
    if(sum == Q):
      return BULLSEYE
    elif(sum < Q):
      return UNDERSHOOT
    else:
      return OVERSHOOT

## Helper functions - end ######################
## Main algorithm - begin ######################
  queue = [[]]
  while(len(queue) is not 0):
    s = queue.pop(0)
    sol = isSolution(s)
    if(sol == BULLSEYE):
      return s
    elif(sol == UNDERSHOOT):
      ext = extendSolution(s)
      queue.extend(ext)
    else:
      pass
  return []
## Main algorithm - end ######################

if __name__ == "__main__":
  print makeChange(80, [10, 4, 6]) 
  print makeChange(80, [1, 4, 6])   #takes too long
  print makeChange(11, [4, 6]) # No solution
