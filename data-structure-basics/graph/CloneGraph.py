# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    
    def __str__(self) -> str:
        return f'{self.label}, [{self.neighbors}]'

from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraphRec(self, node):
        if node is None : return None

        def doClone(node, copyNodeDictionary) :
            copyNode = copyNodeDictionary[node]
            for neighbor in node.neighbors:
                if neighbor in copyNodeDictionary :
                    copyneighbor = copyNodeDictionary[neighbor]
                else :
                    copyneighbor = UndirectedGraphNode(neighbor.label)
                copyNodeDictionary[neighbor] = copyneighbor
                copyNode.neighbors.append(copyneighbor)
                doClone(neighbor, copyNodeDictionary)
        copyRoot = UndirectedGraphNode(node.label)
        copyNodeDictionary = {}
        copyNodeDictionary[node] = copyRoot
        doClone(node, copyNodeDictionary)
        return copyRoot
    
    def cloneGraph(self, node):
         if node is None : return None
         copyNodeDictionary = {}
         copyRoot = UndirectedGraphNode(node.label)
         copyNodeDictionary[node] = copyRoot
         queue = deque()
         queue.append(node)
         while len(queue) > 0 :
             curr = queue.popleft()
             copyNode = copyNodeDictionary[curr]
             for neighbor in curr.neighbors:
                if neighbor in copyNodeDictionary.keys() :
                    copyneighbor = copyNodeDictionary[neighbor]
                    copyNode.neighbors.append(copyneighbor)
                else :
                    copyneighbor = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                    copyNodeDictionary[neighbor] = copyneighbor
                    copyNode.neighbors.append(copyneighbor)
                
         return copyRoot

solution = Solution()
root = UndirectedGraphNode(1)
next1 = UndirectedGraphNode(2)
next2 = UndirectedGraphNode(3)
root.neighbors.append(next1)
root.neighbors.append(next2)
next1.neighbors.append(root)
next1.neighbors.append(next2)
next2.neighbors.append(root)
next2.neighbors.append(next1)

copyGraph = solution.cloneGraph(root)
print(copyGraph)
print(root ==  copyGraph)