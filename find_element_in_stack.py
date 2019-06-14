class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop()
        
    def peek(self):
        return self.stack[-1]


def find_value_in_stack(s,v):
    # if v exists in stack s, return True, else False
    found = False
    temp = Stack()
    while s.isEmpty() == False:
        item = s.peek()
        if item == v:
            found = True
            break
        else:
            temp.push(s.pop())
            
    # reconstruct stack
    while temp.isEmpty() == False:
        s.push(temp.pop())
    return found
    
s =  Stack()
for i in [10,2,3,4,5,8]:
    s.push(i)
    
find_value_in_stack(s,40)
    