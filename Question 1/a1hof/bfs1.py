#!/usr/bin/python
import sys

sys.path.append("../tree")

import tree2 as T

def search(ic, extendSolution, isSolution):
  initialContents = ic
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
