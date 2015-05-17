#!/usr/bin/python
'''
  This version of jugs makes use of the higher-order search function defined in bfs module.
  This function implements the generic breadth first search algorithm.
'''
import sys

sys.path.append("../tree")

import tree2 as T
import bfs1 as bfs

def fillJug(capacities, Q):

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

    nss = []
    # Determine whether a node with the same contents as node n already exists. Return false if yes.
    # True otherwise.
    def isNewContents(n):
      return not T.searchNode(n, T.getContents)

    # process is a higher order function that takes a function g and applies it to each elements
    # in the current state state. Its result is obtained as a side-effect on nss, i.e. after executing
    # it adds elements to nss (defined above) corresponding to executing g on each i of the contents
    # of the current state.
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

  return bfs.search([0] * len(capacities), extendSolution, isSolution)

if __name__ == "__main__":
  print fillJug([6, 6], 6)
  print fillJug([4, 5], 3)
  print fillJug([19, 17, 13], 10)
