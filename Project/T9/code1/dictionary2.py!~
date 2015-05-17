#!/usr/bin/python

import string

class Dictionary:
  def __init__(self, fileName):
    self.words = []
    fin = open(fileName, 'r')
    while(True):
      line = fin.readline()
      if(line == ''):
        break
      else:
        self.words.append(string.strip(line))

  def __str__(self):
    s = ""
    for w in self.words:
      s += w + "\n"
    return s

  # Given a word w, find if w is a prefix of any word in the dictionary.
  def findPrefix(self, w):
    for word in self.words:
      if word[:len(w)] == (w):
        return True
    return False

if __name__ == "__main__":
  dictionary = Dictionary("linux.words.txt")
  print dictionary

  def t1():
    print dictionary.findPrefix("Zur")
    print dictionary.findPrefix("zbcd")

  t1()
