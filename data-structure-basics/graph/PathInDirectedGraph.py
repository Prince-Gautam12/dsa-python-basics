from ScalerGraph import getAdjList
from collections import deque 
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adjList = getAdjList(A, B)
        return self.findPath(adjList, A)

    def findPath(self, graph, target):
        queue = deque()
        visited = set()
        queue.append(1)
        visited.add(1)
        while len(queue) > 0:
            curr = queue.popleft()
            if graph[curr] != None:
                for neighbour in graph[curr]:
                    if neighbour not in visited :
                        if neighbour == target : return 1
                        queue.append(neighbour)
                        visited.add(neighbour)
        return 0


solution = Solution()
print(solution.solve(5, [  [1, 2] ,[4, 1] ,[2, 4] ,[3, 4] ,[5, 2] ,[1, 3] ]))
print(solution.solve(4, [[1,2],[2,3],[4,3]]))
