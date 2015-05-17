#!/usr/bin/python
import sys

import tree2 as T

def fillJug(capacities, Q):

 # A content configuration (e.g. [1, 4, 2]) is a solution if the number of filled jugs is one
 # and it contains Q amount of fluid.
  def isSolution(s):
    def numOfNonEmptyJugs(c):
      def g(x, y):
        if(y == 0): return x
        return x + 1
      return reduce(g, c, 0)

    def totalQuantity(c):
      return reduce(lambda x, y: x + y, c, 0)

    c = T.getContents(s)
    return (numOfNonEmptyJugs(c) == 1) and (totalQuantity(c) == Q)
  
  ##### extendSolution - Begin ##################
  # Given an incomplete solution state, extend it by performing all the atomic operations:
  #   -- Create a new solution by emptying each jug one by one.
  #   -- Create a new solution by filling each jug to its capacity one by one.
  #   -- Create a new solution by transferring the contents of each jug to every other.
  def extendSolution(state):
    contents = T.getContents(state)
    # empty the ith jug.
    def empty(i):
      newcontents = contents[:]
      newcontents[i] = 0
      return newcontents

    # fill the ith jug to its capacity
    def fill(i):
      newcontents = contents[:]
      newcontents[i] = capacities[i]
      return newcontents

    # transfer the contents of jug i to jug j. Do it only if:
    #  -- i is not empty
    #  -- j is not full
    # Transfer only so much as j can hold (in case i holds more fluid than j can take)
    def transfer(i, j):
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

    def isNewContents(n):
      return not T.searchNode(n, T.getContents)

    nss = []
    def process(g):
      for i in range(len(capacities)):
        nc = g(i)
        ns = T.makeLeaf(nc, state)
        if(isNewContents(ns)):
          T.addSubtree(state, ns)
          nss.append(ns)
    
    # Create new states by emptying jug i.
    process(empty)
    # Create new states by filling jug i.
    process(fill)
    # Create new states by transferring i's contents to each other j.
    for i in range(len(capacities)):
      process(lambda n: transfer(i, n))

    return nss
  ##### extendSolution - End ##################

  # Main algorithm - Begin #########################
  initialContents = [0] * len(capacities)
  initialState = T.makeLeaf(initialContents, None) # root state
  queue = [initialState]
  while(len(queue) is not 0):
    s = queue.pop(0)
    if(isSolution(s)):
      strace = T.getTrace(s)
      strace.pop(0)
      return [T.getContents(s) for s in strace]
    es = extendSolution(s)
    queue.extend(es)
  return None
  # Main algorithm - End #########################

if __name__ == "__main__":
  print fillJug([6, 6], 6)
  print fillJug([4, 5], 3)
  print fillJug([19, 17, 13], 10)
  print fillJug([17, 11, 19], 13)
