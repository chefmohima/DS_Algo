# Linked List Implementation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        if self.head is None:
            return True
        return False
        
    def insert_at_head(self,data):
        node = Node(data)
        if self.is_empty() is True:
            self.head = node
        else:
            #next = self.head
            node.next = self.head
            self.head = node
        return self.head
        
    def insert_at_tail(self,data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            # get last node
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        return self.head
        
    def insert_at_index(self,index,data):
        node = Node(data)
        if self.is_empty():
            if index == 1:
                self.head = node
            else:
                print('Index does not exist in list')
                return
        else:
            if index == 1:
                self.head = node
                return self.head
            
            # find node with index-1
            current = self.head
            count = 1
            while count < index-1:
                current = current.next
                count += 1
            if not current:
                print('index does not exist')
                return
            else:
                next = current.next
                current.next = node
                node.next = next
        return self.head
        
    def insert_before_value(self,value,data):
        # find node with data == value
        # keep a ptr to prev node
        prev = None
        current = self.head
        while current.next:
            if current.data == value:
                break
            else:
                prev = current
                current = current.next
        # create new node
        node = Node(data)
        if prev is None:
            self.head = node
            return self.head
        prev.next = node
        node.next = current
        return self.head
        
    def delete_at_head(self):
        self.head = self.head.next
        return self.head
    
    def delete_at_tail(self):
        if self.is_empty():
            print('Empty list, nothing to delete')
            return
        # find last node and keep ptr to previous node
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
            
        # prev is node before last node
        prev.next = None
        return self.head
        
        
    
    def delete_at_index(self,index):
        # find node at index-1
        count = 1
        if index == count:
            # remove head node
            self.delete_at_head()
            return
        current  =self.head
        while count < index-1:
            current = current.next
            count += 1
        if current is None:
            print('index does not exist in the list')
            return
        to_delete = current.next
        current.next = current.next.next
        to_delete.next = None
        return self.head
        
    
            
        
                
        
        
    
         
##Execute methods##
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

ll = LinkedList()
ll.head = node1
ll.insert_at_head(0)
ll.insert_at_tail(5)
#ll.insert_at_index(1,10)
#ll.insert_before_value(4,40)
#ll.delete_at_head()
#ll.delete_at_tail()
ll.delete_at_index(1)