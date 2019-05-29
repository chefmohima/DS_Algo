class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
        
    def get_nth_node(self, n):
        current = self.head
        if current is None:
            print('Empty List')
            return None
        count = 1
        while count < n:
            count += 1
            current = current.next
            if current is None:
                raise IndexError
            
        return current.data
        
# build a list
ll = LinkedList()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

ll.head = node1
ll.get_nth_node(6)




    
    