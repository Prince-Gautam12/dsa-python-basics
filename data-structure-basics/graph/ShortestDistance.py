# Dijkstra algorithm
    # - Sets, dictionary, priority queue (heap), dfs/bfs
    # Greedy algorithm
from queue import PriorityQueue
from Graph import AdjListGraph
class Dijkstra:
    def findMinPathFromSource(self, graph, source):
        pq = PriorityQueue()
        dist =[999999999999]*len(graph)
        dist[source] = 0
        pq.put((0,source, -1))
        while not pq.empty():
            cost, curr, parent  = pq.get()
            for neighbor, nCost in graph[curr]:
                newCost = cost + nCost 
                if neighbor is not parent and dist[neighbor] > newCost:
                    dist[neighbor] = newCost
                    pq.put(( newCost, neighbor, curr))
        return dist
    
adjGraph = AdjListGraph([[1,2,2],[1,6,3],[2,3,3],[2,3,4],[2,5,3],
                         [3,4,1],[4,5,2],[5,6,7],[4,7,3],[7,8,2]],9,True, True)
dijkstra = Dijkstra()
print(dijkstra.findMinPathFromSource(adjGraph.adjList, 5))
