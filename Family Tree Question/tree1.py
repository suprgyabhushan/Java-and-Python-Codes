#!/usr/bin/python

def root(t):
  return t

def subtrees(t):
  (r, st) = t
  return st

def allNodes(t):
  r = root(t)
  st = subtrees(t)
  nodes = [r]
  for s in st:
    nodes.extend(allNodes(s))
  return nodes

def searchNode(n, t):
  nodes = allNodes(t)
  nids = [i for (i, s) in allNodes(t)]
  return n in nids

def makeTree(n, children):
  for c in children:
    if (searchNode(n, c)):
      return None
  return (n, children)

def makeLeaf(n):
  return (n, [])

def allAncestors(n, t):
  if(n == root(t)):
    return []
  else:
    p = parent(n, t)
    a = allAncestors(p, t)
    a.append(p)
    return a
     
def parent(n, t):
  for node in allNodes(t):
    if n in subtrees(node):
      return node
  return None

def depth(n, t):
	return len(allAncestors(n, t))
	
## Test Cases ####
l1 = makeLeaf(1)
l2 = makeLeaf(2)
l3 = makeLeaf(3)
l4 = makeLeaf(4)
l5 = makeLeaf(5)
l6 = makeLeaf(6)

tree1 = makeTree(4, [l1, l2, l3])
tree2 = makeTree(3, [l1, l2, l3])

n7 = makeTree(7, [l1, l2, l3])
n8 = makeTree(8, [l4, l5, l6])
tree3 = makeTree(9, [n7, n8])

def test_makeTree():
  print "**** makeTree - begin ****"
  def t1():
    print "-- t1 - begin"
    print "tree = " + str(tree1)
    print "-- t1 - end"

  def t2():
    print "-- t2 - begin"

    print "tree = " + str(tree2)
    print "-- t2 - end"

  def t3():
    print "-- t3 - begin"
    print "tree = " + str(tree3)
    print "-- t3 - end"
 

  t1()
  t2()
  t3()
  print "**** makeTree - end ****"

def test_allNodes():
  print "**** allNodes - begin ****"
  print allNodes(tree3)
  print "**** allNodes - end ****"


def test_searchNode():
  print "**** searchNode - begin ****"
  print searchNode(9, tree3)
  print searchNode(1, tree3)
  print searchNode(10, tree3)
  print "**** searchNode - end ****"

if __name__ == "__main__":
  test_makeTree()
  test_allNodes()
  test_searchNode()
