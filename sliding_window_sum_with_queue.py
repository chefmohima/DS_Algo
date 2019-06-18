# Queue with list

class Queue:
    def __init__(self,size):
        self.list = []
        #self.num_of_elements = 0
        self.size = size
    
    def getSize(self):
        return len(self.list)
        
    def isEmpty(self):
        return self.list == []
        
    def isFull(self):
        return self.getSize() == self.size
   
    def enqueue(self,item):
        if self.isFull():
            return
        self.list.append(item)
        #self.num_of_elements += 1
        
    def dequeue(self):
        if self.isEmpty():
            return
        item = self.list.pop(0)
        #self.num_of_elements -= 1
        return item
        
def sliding_win(l,k):
    # l is input list and k is length of window
    # find sum of each window
    sum = 0
    q = Queue(k)
    for i in range(len(l)):
        if q.isFull():
            print(sum)
            x = q.dequeue()
            sum -= x
        q.enqueue(l[i])
        sum += l[i]
    print(sum)
            
sliding_win([1,2,3,4,6,8,12],3)
        
        
        