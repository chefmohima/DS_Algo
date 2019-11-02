# Min heap implementation

class minHeap:
  def __init__(self):
    self.heap = []
    
  def insert(self,val):
    self.heap.append(val)
    if len(self.heap) > 1:
        self.restoreUp(len(self.heap)-1)
  
  def getMin(self):
      if self.heap:
          return self.heap[0]
      return None
      
    
  def removeMin(self):
      if len(self.heap) > 1:
          min = self.heap[0]
          # swap min with last element
          self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
          del(self.heap[-1])
          self.restoreDown(0)
          return min
      if len(self.heap) == 1:
          return self.heap[0]
          del(self.heap[0])
      else:
          return None
    
    
  
  def restoreUp(self, index):
      # compare with parent and swap as necessary
      # continue till parent exists and parent > value at index
      parent_index = (index-1)//2
      if parent_index>=0 and self.heap[parent_index] > self.heap[index]:
          self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
          self.restoreUp(parent_index)
    
    
  def restoreDown(self,index):
      minindex = index
      leftindex = 2*index +1
      rightindex = 2*index + 2
      if rightindex <= len(self.heap)-1:
          # find minimum
          if self.heap[leftindex] < self.heap[minindex]:
              minindex = leftindex
          if self.heap[rightindex] < self.heap[minindex]:
              minindex = rightindex
              
      if minindex != index:
          # need to swap
          self.heap[minindex], self.heap[index] = self.heap[index], self.heap[minindex]
          self.restoreDown(minindex)
    
  
heap = minHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMin())
print(heap.removeMin())
print(heap.getMin())
heap.insert(-100)
print(heap.getMin())
