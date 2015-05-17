#!/usr/bin/python
import tree1 as T

## Family Tree Application Programming Interface

def areSiblings(n1, n2, F):
  return T.parent(n1, F) == T.parent(n2, F)

def areCousins(n1, n2, F):
  return (not areSiblings(n1, n2, F)) and (T.depth(n1, F) == T.depth(n2, F))

## Test Cases ####
def test_familytree():
  manas    = T.makeLeaf("Manas")
  tapas    = T.makeLeaf("Tapas")
  olivia   = T.makeLeaf("Olivia")
  abhinav  = T.makeLeaf("Abhinav")
  aakash   = T.makeLeaf("Aakash")
  agni     = T.makeLeaf("Agni")
  vidyut   = T.makeLeaf("Vidyut")
  armaan   = T.makeLeaf("Armaan")
  vigyan   = T.makeLeaf("Vigyan")

  mridula  = T.makeTree("Mridula", [manas, tapas])
  purnima  = T.makeTree("Purnima", [abhinav, olivia])
  sushma   = T.makeTree("Sushma", [aakash, agni])
  mantosh  = T.makeTree("Mantosh", [armaan])
  amitabh  = T.makeTree("Amitabh", [vidyut])
  sujit    = T.makeTree("Sujit", [vigyan])
  shatabdi = T.makeLeaf("Shatabdi")
  sonali   = T.makeLeaf("Sonali")
  
  shefali  = T.makeTree("Shefali", [mridula, purnima, sushma])
  jharna   = T.makeTree("Jharna", [amitabh, sujit])
  bani     = T.makeTree("Bani", [shatabdi, sonali])
 
  sudha    = T.makeTree("Sudha", [shefali, jharna, bani])
  sneha    = T.makeTree("Sneha", [sudha])

  family   = sneha

  def test_areSiblings():
    def t1():
      print (areSiblings(amitabh, sujit, family))
    def t2():
      print (areSiblings(shatabdi, sonali, family))
    def t3():
      print (areSiblings(amitabh, manas, family))

    t1()
    t2()
    t3()

  def test_areCousins():
    def t1():
      print (areCousins(amitabh, sujit, family))
    def t2():
      print (areCousins(shatabdi, sonali, family))
    def t3():
      print (areCousins(amitabh, manas, family))
    def t4():
      print (areCousins(abhinav, manas, family))

    t1()
    t2()
    t3()
    t4()

#  test_areSiblings()
  test_areCousins()

if __name__ == "__main__":
  test_familytree()
