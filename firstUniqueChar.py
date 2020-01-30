# Implement a function, findFirstUnique(lst) that returns the first unique integer in the list.
# Input : [9,2,3,2,6,6], Output: 9
import pytest

def findFirstUniquebruteforce(lst):
  # Write your code here
  
  unique = []
  for i in range(len(lst)):
    notUnique = False
    for j in range(i+1, len(lst)):
      if lst[i] == lst[j]:
          notUnique = True
          break
    if not notUnique:
      return lst[i]
    
  return None
  
  
def findFirstUnique(lst):
  # Write your code here
  charCounter = {}
  for idx in range(len(lst)):
      if lst[idx] in charCounter:
          # flag as non-unique
          charCounter[lst[idx]] = 'NOTUNIQUE'
      else:
          charCounter[lst[idx]] = idx
  uniqueNumIndices = [v for v in d.values() if v != 'NOTUNIQUE']
  if uniqueNumIndices:
      return lst[min(uniqueNumIndices)]
  return -1  
 
 
 def test_findFirstUnique():
     assert findFirstUnique([9,2,3,2,6,6]) == 9
  
 