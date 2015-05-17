#!/usr/bin/python

# create a new state with the state p as its parent
def makeTree(c, st, p):
  return (c, st, p)

def makeLeaf(c, p):
  return makeTree(c, [], p)

def getContents(s):
  (c, nss, p) = s
  return c

def getSubtrees(s):
  (c, nss, p) = s
  return nss

def parent(s):
  (c, nss, p) = s
  return p

def addSubtree(s, ns):
  (c, nss, p) = s
  nss.append(ns)

def root(s):
  p = parent(s)
  if(p == None):
    return s
  return root(p)

def getTrace(s):
  p = parent(s)
  if(p == None):
    return [s]
  ptrace = getTrace(p)
  ptrace.append(s)
  return ptrace

def depth(n):
  p = parent(n)
  if(p == None):
    return 0
  else:
    return 1 + depth(p)

# If such a node exists return True. Otherwise return False (meaning that n is a new state)
# The function first finds out the root node of the node tree by calling root.
# This assumes that n already has a meaningful parent node.
# Using a recursive helper function searchNodeInTree, the function determines if such a
# state exists in the subtree.
# Also, the function uses the user provided identity function to compute the identity of the node, and
# hence its equality with other nodes.
def searchNode(n, fid):
  def searchNodeInTree(r, n):
    if(fid(r) == fid(n)):
      return True
    for ns in getSubtrees(r):
      if(searchNodeInTree(ns, n)):
        return True
    return False
  r = root(n)
  return searchNodeInTree(r, n)

