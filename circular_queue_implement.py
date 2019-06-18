# Circular Queue Implementation

class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.num_of_elements = 0
        self.list = [None]*size
        self.front = 0
        self.back = 0
        
    def enqueue(self,item):
        # check if queue has space
        if self.num_of_elements >= self.size:
            print('Queue out of space')
            return
        else:
            # place item at back
            self.list[self.back] = item
            # circularly increment back ptr
            self.back = (self.back+1)%self.size
            self.num_of_elements += 1
            
    def dequeue(self):
        # check if queue is empty
        if self.num_of_elements == 0:
            print('Nothing to dequeue')
            return
        else:
            # dequeue from front
            self.front = (self.front+1)%self.size
            self.num_of_elements -= 1
            
    
# Execute
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)       # out of space error
cq.dequeue()
cq.enqueue(6)       # 6->2->3->4->5


