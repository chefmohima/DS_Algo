# DFS traversal

class Node:
    def __init__(self,data,connections=None,explored=False):
        self.data = data
        self.explored = explored
        if connections is None:
            self.connections = []
        else:
            self.connections = connections
            
    def add_connection(self,node):
        
        self.connections.append(node)
        
    def get_connections(self):
        return self.connections
        
def dfs_traverse(node):
    print(node.data)
    node.explored = True
    connections =  node.get_connections()
    for conn in connections:
        if conn.explored == False:
            dfs_traverse(conn)
            
# Test Code
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeA.add_connection(nodeB)
nodeA.add_connection(nodeC)
nodeB.add_connection(nodeE)
nodeC.add_connection(nodeD)
nodeD.add_connection(nodeE)


dfs_traverse(nodeA)