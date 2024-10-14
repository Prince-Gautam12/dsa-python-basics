from ScalerGraph import getAdjListFromArray
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
    def solve(self, A, B, C):
        adjList = getAdjListFromArray(len(A), A)
        def dfs(curr, graph, visited, dest):
            if curr == dest:
                return True
            visited.add(curr)
            ans = False
            if graph[curr] != None:
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        ans = ans or dfs(neighbour, graph, visited, dest)
            return ans
        ans = dfs(C, adjList, set(), B)
        if ans:
            return 1
        else:
            return 0 
    
solution = Solution()
print(solution.solve([1, 1, 2], 1, 2))
print(solution.solve([1, 1, 2], 2, 1))
print(solution.solve([1,1,1,3,3,2,2,7,6], 3, 8))
	
            