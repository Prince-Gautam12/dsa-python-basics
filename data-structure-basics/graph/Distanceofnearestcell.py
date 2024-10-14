from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        def updateDistInRes(row, col, dist, A, result, queue):
            if row < 0 or row >= len(A) or col < 0 or col >= len(A[row]) or A[row][col] == 1: return
            result[row][col] = min(result[row][col], dist)
            queue.append([row,col,dist])
            A[row][col] = 1 

        N = len(A)
        M = len(A[0])
        result = [[0] * M for _ in range(N)]
        queue = deque()
        for row in range(0, len(A)):
            for col in range(0, len(A[row])):
                if 1 == A[row][col]:
                    queue.append([row, col, 0])
                else : result[row][col] = 9999999999999999999
        
        while len(queue) > 0:
            curr = queue.popleft()
            row,col,dist = curr[0],curr[1], curr[2]
            updateDistInRes(row-1, col, dist+1, A,result, queue)
            updateDistInRes(row+1, col, dist+1,A,  result, queue)
            updateDistInRes(row, col-1, dist+1,A, result, queue)
            updateDistInRes(row, col+1, dist+1,A, result, queue)
        return result
    
solution = Solution()
print(solution.solve([
       [0, 0, 0, 1],
       [0, 0, 1, 1], 
       [0, 1, 1, 0]
     ]))

print(solution.solve([
       [1, 0, 0, 0],
       [0, 0, 0, 0], 
       [0, 0, 0, 0]
     ]))