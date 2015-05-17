#!/usr/bin/python

import t9slow
import t9fast
def t(s):
  tnineslow = t9slow.T9()
  tninefast = t9fast.T9()
  tnineslow.inputString(s)
  tninefast.inputString(s)
  return set(tnineslow.currentPrefixes) == set(tninefast.currentPrefixes) and set(tnineslow.getCurrentPrefix()) == set(tninefast.getCurrentPrefix())

if __name__ == "__main__":
  strings = ["23"]
  for s in strings:
    print t(s)

