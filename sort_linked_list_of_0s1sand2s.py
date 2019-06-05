# Linked List Implementation
# for problems where nodes have to be rearranged

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
        
def sort_list(l):
    # given a linked list of 0, 1 and 2 .
    # sort these nodes so that all 0s first, then all 1s and then all 2s
    l0 = LinkedList()
    l1 = LinkedList()
    l2 = LinkedList()
    
    # traverse input list and append each node to appropriate list
    current = ll.head
    if current is None:
        print('Empty List')
        return l0
    while current:
        if current.data == 0:
            dest_list = l0
        elif current.data == 1:
            dest_list = l1
        else:
            dest_list = l2
            
        dest_list.append(current)
        current = current.next
    l0.tail.next  =None
    l1.tail.next = None
    l2.tail.next = None
        
    # now that all the values are in separate lists, combine the 3 lists
    l0.append(l1.head)
    l1.append(l2.head)
    return l0
        
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
sort_list(ll)
