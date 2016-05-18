#!/usr/bin/python

def power_product(a, b, x, y):
  return (a ** x) * (b ** y)

def extendSolutions(a, b, prod):
  eprods = []
  eprods.append(prod * a)
  eprods.append(prod * b)
  eprods.append(prod * a * b)
  return eprods

def findPowerProducts(a, b, n):
  queue = [1]
  products = []
  while(len(queue) != 0):
    prod = queue.pop(0)
    if(prod not in products):
      products.append(prod)
    if(len(products) == n):
      return products
    eprods = extendSolutions(a, b, prod)
    queue.extend(eprods)
    queue.sort() # this statement makes sure that the least value is at the beginning of the queue.
  
if __name__ == "__main__":
  print findPowerProducts(5, 2, 10)
