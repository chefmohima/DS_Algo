class Stack:
    def __init__(self):
        self.list = []
        
    def isEmpty(self):
        return len(self.list) == 0
        
    def push(self,item):
        self.list.append(item)
        return
    
    def pop(self):
        if self.isEmpty():
            return
        else:
            item = self.list.pop()
            return item
            
class QueueFromStack:
    # assume main stack has all queue elements
    def __init__(self):
        self.main = Stack()
        self.temp = Stack()
        
    def enqueue(self,item):
        while self.main.isEmpty == False:
            self.temp.push(main.pop())
        self.main.push(item)
        while self.temp.isEmpty == False:
            self.main.push(temp.pop())
        return
    
    def dequeue(self):
        if self.main.isEmpty():
            return -1
        else:
            item = self.main.pop()
            return item
            

        