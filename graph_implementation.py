# Graph Implementation

class Node:
    # data is value of the node and 
    # connections will be list of connected nodes
    def __init__(self, data, connections=None):
        self.data = data
        if connections is None:
            self.connections = []
            
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
            conn_list.append(conn.data)
        return conn_list
            
        
        
        
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

nodeA.add_connection('F')
print(nodeA.get_connections())
nodeA.set_data('a')
print(nodeA.get_data())
g = Graph([nodeA,nodeB,nodeC,nodeD,nodeE])
print(g.get_nodes())
        
        
        
        
            


        
        