# Implement 2 stacks using a list

class TwoStacks:
    def __init__(self,n):
        self.list = [None]*n
        self.size = n
        self.s1 = -1
        self.s2 = n
        
    def push_stack1(self, item):
        # check if there is space
        if self.s1 < self.s2-1:
            self.s1 = self.s1 + 1
            self.list[self.s1] = item
        else:
            print('Stack Overflow')
            return
    
    def push_stack2(self, item):
        # check for space
        if self.s1 < self.s2-1:
            self.s2 = self.s2-1
            self.list[self.s2] = item
        else:
            print('Stack Overflow')
            return
    
    def pop_stack1(self):
        if self.s1 > -1:
            item = self.list[self.s1]
            self.s1 = self.s1-1
            return item
        else:
            print('stack underflow')
            return
    
    def pop_stack2(self):
        if self.s2 < self.size:
            item = self.list[self.s2]
            self.s2 = self.s2+1
            return item
        else:
            print('stack underflow')
            return
        
s = TwoStacks(5)
s.push_stack1(1)
s.push_stack2(2)
s.push_stack1(3)
s.push_stack1(4)
s.push_stack2(5)
s.pop_stack1()
s.push_stack1(6)
            
            
            
    
    