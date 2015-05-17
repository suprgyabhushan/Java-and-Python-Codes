#!/usr/bin/python
import sys

sys.path.append("../tree")
import tree2 as T

# Return a function that extends the solution by creating new leaf nodes corresponding to 
# all possible actions that can be taken at the state corresponding to node n.
# The various choices are represented by the list choices. The actions that can be done
# on each of these choices is carried out by the procedure process.
def makeExtendSolution(choices, process, shouldBeAdded):
  def extendSolution(n):
    nss = []
    for i in choices:
      ncs = process(i)
      for nc in ncs: 
        st = T.makeLeaf(nc, n)
        if(shouldBeAdded(st)):
          T.addSubtree(n, st)
          nss.append(st)
    return nss
  return extendSolution
  
  def isSolution(n):
    return getValue(n) == Q

# Polymorphic breadth first search
def search(ic, extendSolution, isSolution):
  initialState = T.makeLeaf(ic, None) # root state
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
