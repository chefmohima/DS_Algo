# Problem: Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
# Solved using BFS
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        map = {}
        q = []
        q.append(node)
        map[node] = Node(node.val,[])
        
        while q:
            v = q.pop(0)
            for n in v.neighbors:
                if n not in map:
                    map[n] = Node(n.val,[])
                    q.append(n)
                map[v].neighbors.append(map[n])
        return map[node]
        
        