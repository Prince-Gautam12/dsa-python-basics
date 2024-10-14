from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        i,j = 0,0
        queue = deque()
        numberOfIsland = 0
        for i in range(0, len(A)):
            for j in range(0,len(A[i])):
                if A[i][j] == 1:
                    queue.append({'row': i,'col':j})
                    A[i][j] = -1
                    numberOfIsland += 1
                    while len(queue) > 0:
                        curr = queue.popleft()
                        self.addCurrNeighbours(queue, curr['row'], curr['col'], A)
        return numberOfIsland
    
    def addCurrNeighbours(self, queue, row, col, A):
        if row > 0 and A[row-1][col] == 1:
            queue.append({'row':row-1, 'col':col})
            A[row-1][col] = -1
        if row > 0 and col > 0 and A[row-1][col-1] == 1:
            queue.append({'row':row-1, 'col':col-1})
            A[row-1][col-1] = -1
        if row > 0 and col < len(A[row])-1 and A[row-1][col+1] == 1:
            queue.append({'row':row-1, 'col':col+1})
            A[row-1][col+1] = -1
        if col > 0 and A[row][col-1] == 1:
            queue.append({'row':row, 'col':col-1})
            A[row][col-1] = -1
        if col < len(A[row])-1 and A[row][col+1] == 1:
            queue.append({'row':row, 'col':col+1})
            A[row][col+1] = -1
        if row < len(A)-1 and A[row+1][col] == 1:
            queue.append({'row':row+1, 'col':col})
            A[row+1][col] = -1
        if row < len(A)-1 and col < len(A[row])-1 and  A[row+1][col+1] == 1:
            queue.append({'row':row+1, 'col':col+1})
            A[row+1][col+1] = -1
        if row < len(A)-1 and col > 0 and A[row+1][col-1] == 1:
            queue.append({'row':row+1, 'col':col-1})
            A[row+1][col-1] = -1


solution = Solution()
print(solution.solve([ 
       [0, 1, 0]
       ,[0, 0, 1]
       ,[1, 0, 0]
     ]))

print(solution.solve([   
       [1, 1, 0, 0, 0]
       ,[0, 1, 0, 0, 0]
       ,[1, 0, 0, 1, 1]
       ,[0, 0, 0, 0, 0]
       ,[1, 0, 1, 0, 1]    
     ]))