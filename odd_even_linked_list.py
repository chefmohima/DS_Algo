# odd even linked list
# rearrange list so that all even indexed nodes come before odd index nodes
# example : input :0->1->0->2->1 output: 1->2->0->0->1

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def get_data(self):
        return self.data
        
    def set_data(self,data):
        self.data = data
        
    def get_next(self):
        return self.next
        
    def set_next(self,node):
        self.next = node
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail = None
        
    def get_head(self):
        return self.head
        
    def get_tail(self):
        return self.tail
        
    def set_head(self,node):
        self.head = node
    
    def set_tail(self,node):
        self.tail = node
        
    def append(self,node):
        # add node at tail
        if self.head is None:
            self.head = node
        else:
            self.tail.next=node
        self.tail = node
        
def odd_even(l):
    # rearrange list so that all even index nodes precede all odd index nodes
    current = l.head
    if current is None:
        return None
    l_odd = LinkedList()
    l_even = LinkedList()
    index = 1               # count of nodes starts with 1 and not 0
    while current:
        if index % 2 == 0:
            l_even.append(current)
        else:
            l_odd.append(current)
        current = current.next
        index += 1
    # merge l_odd and l_even
    l_odd.tail.next=None
    l_even.tail.next= None
    l_even.append(l_odd.head)
    return l_even
    
            
   
        
ll = LinkedList()
node1 = Node(0)
node2 = Node(1)
node3 = Node(0)
node4 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4
ll.set_head(node1)
ll.set_tail(node4)
ll.append(Node(1))
odd_even(ll)

