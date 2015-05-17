#!/usr/bin/python

import string
def makeleaf(t):
    return[t,[]]
def findchar(lst,ch):
    y=0
    for i in lst:
        if(i[0]==ch):
            return True,y
        y=y+1
    return False,y
def maketree(lst):
    result=['$',[]]
    for w in lst:
        t=result[1]
        for i in w:
            check,y=findchar(t,i)
            if(check==True):
                t=t[y][1]
            else:
                t.append(makeleaf(i))
                t=t[y][1]
    return result            
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
    self.words=maketree(self.words) 
  '''def __str__(self):
    s = ""
    for w in self.words:
      s += w + "\n"
    return s'''
#    s=maketree(self.words)
#    return s

  # Given a word w, find if w is a prefix of any word in the dictionary.
  def findPrefix(self, w):
    t=self.words[1]
    for i in w:
        check,y=findchar(t,i)
        if(check==True):
            t=t[y][1]
        else:
            return False
    return True

if __name__ == "__main__":
  dictionary = Dictionary("linux.words.txt")
  

  def t1():
    print dictionary.findPrefix("Zur")
    print dictionary.findPrefix("zbcd")

  t1()
