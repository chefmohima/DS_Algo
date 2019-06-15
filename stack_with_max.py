# Implement a stack so that we can always get its max value with a function

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
            
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.list[-1]
        
class StackWithMax:
    
    def __init__(self):
        self.mainstack = Stack()
        self.maxstack = Stack()
        
    def push(self,item):
        if self.mainstack.isEmpty() or item > self.maxstack.peek():
            self.mainstack.push(item)
            self.maxstack.push(item)
        
        else:
            self.mainstack.push(item)
    
    def pop(self):
        if self.mainstack.isEmpty() == False:
            item = self.mainstack.pop()
        if item == self.maxstack.peek():
            self.maxstack.pop()
        return item
        
    def max_value(self):
        return self.maxstack.peek()
        
        
s = StackWithMax()
s.push(1)
s.push(20)
s.push(50)
s.push(5)
s.push(6)

s.max_value()
                

        