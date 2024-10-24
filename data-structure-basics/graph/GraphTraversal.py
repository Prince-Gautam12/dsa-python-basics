from collections import deque 
from Graph import AdjListGraph

class GraphTaversal:
    def bfs(self, graph):
        queue = deque()
        visited = set()
        queue.append(0)
        visited.add(0)
        while len(queue) > 0:
            curr = queue.popleft()
            for neighbour in graph[curr]:
                if neighbour not in visited :
                    queue.append(neighbour)
                    visited.add(neighbour)
            print(curr)
            
        

    # with recursion
    def dfs(self, graph):
        def rec(curr, graph, visited):
            print(curr)
            visited.add(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    rec(neighbour, graph, visited)
            
        visited = set()
        rec(0, graph, visited)


    def bfsMultiComponent(self, graph, noOfNodes):
        queue = deque()
        visited = set()
        for i in range(noOfNodes):
            if i in visited: continue
            queue.append(i)
            visited.add(i)
            while len(queue) > 0:
                curr = queue.popleft()
                for neighbour in graph[curr]:
                    if neighbour not in visited :
                        queue.append(neighbour)
                        visited.add(neighbour)
                print(curr)
    
    def dfsMultiComponent(self, graph, noOfNodes):
        pass
                
            

# A-B
# A-C
# B-D
# C-D
# C-E
# E-F
# F-G
# F-H
class TraversalDemo:
    def demo(self):
        graphTraversal = GraphTaversal()
        adjListGraph = AdjListGraph([[0,1],[0,2],[1,3],[2,3],[2,4],[4,5],[5,6],[6,7]], 8, True)
        adjListGraph.print()
        graphTraversal.bfs(adjListGraph.adjList)
        print("====== DFS =======")
        graphTraversal.dfs(adjListGraph.adjList)
        print("==== BFS MC ======")
        graphTraversal.bfsMultiComponent(AdjListGraph([[0,1],[2,3]], 4, True).adjList, 4)

traversal = TraversalDemo()
traversal.demo()