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
        
    def delete_node(self,node):
        # in O(1) time, no prev node needed
        # copy next node's data into the current node, then delete the next node
        node.set_data(node.next.get_data())
        node.next  = node.next.next
        
        
    
def find_nth_node_from_end(l,n):
    slow_ptr = fast_ptr = l.head
    # create a difference of n-1 between the fast and slow ptr
    # then move both slow and fast by 1 till fast is at end node
    # then slow must point at nth node from end
    for i in range(1,n):
        fast_ptr = fast_ptr.next
        
    while fast_ptr.next:
        fast_ptr=fast_ptr.next
        slow_ptr=slow_ptr.next
    return slow_ptr.data
        
            
   
        
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
ll.append(Node(5))

# 0->1->0->2->5: second from end = 2
find_nth_node_from_end(ll,2)