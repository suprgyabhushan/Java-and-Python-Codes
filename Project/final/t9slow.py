#!/usr/bin/python

import dictionary1 as D

class T9:
  def __init__(self):
    self.dictionary = D.Dictionary("linux.words.txt")
    self.reset()
    self.keymap = {
      "2" : ["a", "b", "c", "A", "B", "C"],
      "3" : ["d", "e", "f", "D", "E", "F"],
      "4" : ["g", "h", "i", "G", "H", "I"],
      "5" : ["j", "k", "l", "J", "K", "L"],
      "6" : ["m", "n", "o", "M", "N", "O"],
      "7" : ["p", "q", "r", "s", "P", "Q", "R", "S"],
      "8" : ["t", "u", "v", "T", "U", "V"],
      "9" : ["w", "x", "y", "z", "W", "X", "Y", "Z"]
    }

  def reset(self):
    self.keypresses      = []
    self.currentIndex    = 0
    self.currentPrefixes = [""]

  # returns the current prefix
  def getCurrentPrefix(self):
    return self.currentPrefixes[self.currentIndex]

  # Increment the current prefix index by 1. Cycle around if required.
  def incrementIndex(self):
    self.currentIndex += 1
    if(self.currentIndex == len(self.currentPrefixes)):
      self.currentIndex = 0

  # Decrement the current prefix index by 1. Cycle around if required.
  def decrementIndex(self):
    self.currentIndex -= 1
    if(self.currentIndex == -1):
      self.currentIndex = len(self.currentPrefixes) - 1

  # Return the set of new prefixes with 'letter' appended to all the current prefixes
  def getNewPrefixes(self, letter):
    candidatePrefixes = [prefix + letter for prefix in self.currentPrefixes]
    newPrefixes = filter(self.dictionary.findPrefix, candidatePrefixes)
    return newPrefixes

  # Update the set of current prefixes with the numeric key k.
  def computeCurrentPrefixes(self, k):
    letters = self.keymap[k]
    newPrefixes = []
    for l in letters:
      newPrefixes.extend(self.getNewPrefixes(l))
    self.currentPrefixes = newPrefixes

  # Recompute the list of current prefixes based on the current value of self.keypresses.
  def updateCurrentPrefixes(self):
    self.currentIndex    = 0
    self.currentPrefixes = [""]
    
    for k in self.keypresses:
      self.computeCurrentPrefixes(k)

  # Given a single key k, set the values of instance attributes as follows:
  # - self.currentPrefixes : The current list of prefixes which correspond to the keypresses
  def inputKey(self, k):
    if( (k == "2") or (k == "3") or
        (k == "4") or (k == "5") or (k == "6") or 
        (k == "7") or (k == "8") or (k == "9") ):
      self.computeCurrentPrefixes(k)
      self.keypresses.append(k)
    elif(k == "b"):
      if(len(self.keypresses) != 0):
        self.keypresses.pop()
        self.updateCurrentPrefixes()
    elif(k == "p"):
      self.decrementIndex()
    elif(k == "n"):
      self.incrementIndex()
    elif(k == "r"):
      self.reset()
    else:
      pass

  # Given a string s, set the values of the instance attributes as would be on invoking inputKey
  # with each character in s in order.
  def inputString(self, s):
    self.reset()
    for c in s:
      self.inputKey(c)

if __name__ == "__main__":
  t9 = T9()
#  t9.inputKey('2')
#  t9.inputKey('2')
#  t9.inputKey('2')
#  t9.inputKey("9")
#  t9.inputKey("8")
#  t9.inputKey("7")
#  t9.inputKey("4")
#  t9.inputKey("2")
#  t9.inputKey("4")
  t9.inputString("987424")
  t9.inputKey("r")
  t9.inputString("987")
  t9.inputKey("b")
  print t9.currentPrefixes
  print t9.keypresses
