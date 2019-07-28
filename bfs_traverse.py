# BFS Implementation

class Node:
    # data is value of the node and 
    # connections will be list of connected nodes
    # the explored attribute is only for traversals to mark a node 
    # as already traversed
    def __init__(self, data, connections=None, explored=False):
        self.data = data
        if connections is None:
            self.connections = []
        self.explored = explored
            
    def get_data(self):
        return self.data
    
    def set_data(self,data):
        self.data = data
        
    def add_connection(self, data):
        node = Node(data)
        self.connections.append(node)
        
    def get_connections(self):
        conn_list = []
        for conn in self.connections:
            conn_list.append(conn)
        return conn_list
            
        
        
# graph class is not used as bfs will just take the starting node as argument
# and not entire graph        
class Graph:
    def __init__(self,node_list=None):
        if node_list is None:
            self.node_list = []
        else:
            self.node_list=node_list
            
    def get_nodes(self):
        nodes = [node.data for node in self.node_list]
        return nodes
        
    def add_node(self,data):
        node = Node(data)
        self.node_list.append(node)
        
    def get_edges(self):
        edges = []
        for node in self.node_list:
            connections = node.get_connections()
            for conn in connections:
                edges.append((node.data,conn))
        return edges
        
# Queue structure to implement bfs
class Queue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
        
    def enqueue(self,element):
        self.elements.append(element)
        
    def dequeue(self):
        if self.is_empty() == False:
            element = self.elements.pop(0)
            return element
        

# bfs traversal function        
def bfs_traverse(start_node):
    q = Queue()
    q.enqueue(start_node)
    start_node.explored = True
    while q.is_empty() == False:
        s = q.dequeue()
        print(s.data)
        for node in s.get_connections():
            if node.explored == False:
                q.enqueue(node)
                node.explored = True

        
# Test code
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')

nodeA.connections=[nodeB,nodeC]
nodeB.connections=[nodeA,nodeC]
nodeC.connections=[nodeA,nodeB,nodeD]
nodeD.connections=[nodeC,nodeE]
nodeE.connections=[nodeB,nodeD]

bfs_traverse(nodeA)



        
        
        
        
            


        
        