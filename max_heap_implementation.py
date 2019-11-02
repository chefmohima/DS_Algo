# Max Heap Implementation

class maxHeap:
  def __init__(self):
      self.heap = []
      #return self.heap

    
  def insert(self,val):
      self.heap.append(val)
      index = len(self.heap)-1
      self.restoreUp(index)
    
  
  def getMax(self):
      if not self.heap:
          return None
      return self.heap[0]
    
  
  def removeMax(self):
      if not self.heap:
          return None
      if len(self.heap) == 1:
          value =  self.heap[0]
          del(self.heap[0])
          return value
      # swap with last element
      if len(self.heap) > 1:
          self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
          del(self.heap[-1])
      # restore down till the node is at its right place
          self.restoreDown(0)
          return value
          
      
    
  
  def restoreUp(self, index):
      parent_index = (index-1)//2
      # loop only till index > 0
      if index > 0 and self.heap[parent_index] < self.heap[index]:
          self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
          self.restoreUp(parent_index)
          
    
    
  def restoreDown(self,index):
      maxindex = index
      leftindex = 2*index +1
      rightindex = 2*index +2
      if rightindex < len(self.heap):
          if self.heap[leftindex] > self.heap[maxindex]:
              maxindex = leftindex
          if self.heap[rightindex] > self.heap[maxindex]:
              maxindex = rightindex
      if maxindex != index:
          # swap
          self.heap[maxindex], self.heap[index] = self.heap[index], self.heap[maxindex]
          restoreDown(maxindex)
          
    
  
heap = maxHeap()
heap = maxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMax())
