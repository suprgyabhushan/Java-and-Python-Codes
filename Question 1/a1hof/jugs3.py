#!/usr/bin/python
'''
  This version of jugs makes use of the higher-order search function defined in bfs module.
  This function implements the generic breadth first search algorithm.
'''
import sys

sys.path.append("../tree")

import tree2 as T
import bfs2 as bfs

def fillJug(capacities, Q):

  INITACTION     = 0
  EMPTYACTION    = 1
  FILLACTION     = 2
  TRANSFERACTION = 3

  def getValueFromContents(contents):
    values = []
    value = [0] * len(capacities)
    for content in contents:
      if(content[0] == EMPTYACTION):
        value = empty(content[1], value)
      elif(content[0] == FILLACTION):
        value = fill(content[1], value)
      elif(content[0] == TRANSFERACTION):
        value = transfer(content[1][0], content[1][1], value)
      else:
        pass
      values.append(value)
    return values

  # 
  def getValue(n):
    ntrace = T.getTrace(n)
    contents = [T.getContents(n1) for n1 in ntrace]
    return getValueFromContents(contents)[-1]

  def isSolution(s):
    def numOfNonEmptyJugs(c):
      def g(x, y):
        if(y == 0): return x
        return x + 1
      return reduce(g, c, 0)

    def totalQuantity(c):
      return reduce(lambda x, y: x + y, c, 0)

    v = getValue(s)
    return (numOfNonEmptyJugs(v) == 1) and (totalQuantity(v) == Q)

  # empty the ith jug.
  def empty(i, contents):
    newcontents = contents[:]
    newcontents[i] = 0
    return newcontents

  # fill the ith jug to its capacity
  def fill(i, contents):
    newcontents = contents[:]
    newcontents[i] = capacities[i]
    return newcontents

  # transfer the contents of jug i to jug j. Do it only if:
  #  -- i is not empty
  #  -- j is not full
  # Transfer only so much as j can hold (in case i holds more fluid than j can take)
  def transfer(i, j, contents):
    def min(x, y):
      if(x < y): return x
      return y

    def isEmpty(i): return contents[i] == 0
    def isFull(i):  return contents[i] == capacities[i]

    newcontents = contents[:]
    if(not (isEmpty(i) or isFull(j))):
      q = min(contents[i], capacities[j] - contents[j])
      newcontents[i] -= q
      newcontents[j] += q
    return newcontents

  def process(i):
    nss = []
    ns = (EMPTYACTION, i)
    nss.append(ns)
    ns = (FILLACTION, i)
    nss.append(ns)
    for j in range(len(capacities)):
      if(i != j):
        ns = (TRANSFERACTION, (i, j))
        nss.append(ns)
    return nss

  # Determine whether a node with the same contents as node n already exists.
  def isNewContents(n): return not T.searchNode(n, getValue)

  # Criterion for adding a particular configuration into the BFS queue: The set of jug-contents should never 
  # have happened so far.
  def shouldBeAdded(n): return isNewContents(n)

  extendSolution = bfs.makeExtendSolution(range(len(capacities)), process, shouldBeAdded)
  
  ##### extendSolution - End ##################

  result = bfs.search((INITACTION, None), extendSolution, isSolution)
  return getValueFromContents(result)
 
if __name__ == "__main__":
  print fillJug([6, 6], 6)
  print fillJug([4, 5], 3)
  print fillJug([19, 17, 13], 10)
