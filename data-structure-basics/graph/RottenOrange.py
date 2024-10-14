# Problem Description
# Given a matrix of integers A of size N x M consisting of 0, 1 or 2.
# Each cell can have three values:

# The value 0 representing an empty cell.
# The value 1 representing a fresh orange.
# The value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

# Example Input
# Input 1:

# A = [   [2, 1, 1]
#         [1, 1, 0]
#         [0, 1, 1]   ]
# Input 2:

 
# A = [   [2, 1, 1]
#         [0, 1, 1]
#         [1, 0, 1]   ]


# Example Output
# Output 1:

#  4
# Output 2:

#  -1

from collections import deque

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        queue = deque()
        maxTime = 0
        countOf1s = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[i])):
                if A[i][j] == 2:
                    queue.append({'row':i,'col':j,'time':0})
                if A[i][j] == 1:
                    countOf1s +=1 
        
        while len(queue) > 0:
            curr = queue.popleft()
            maxTime = max(maxTime, curr['time'])
            if self.addNeighbour(curr['row']-1, curr['col'], curr['time']+1, A, queue) : countOf1s-=1
            if self.addNeighbour(curr['row']+1, curr['col'], curr['time']+1, A, queue) : countOf1s-=1
            if self.addNeighbour(curr['row'], curr['col']-1, curr['time']+1, A, queue) : countOf1s-=1
            if self.addNeighbour(curr['row'], curr['col']+1, curr['time']+1, A, queue) : countOf1s-=1
        
        if countOf1s == 0 :
            return maxTime
        else :
           return -1
        
        
    def addNeighbour(self, row, col, time, A, queue):
        #  Not a valid neighbour
        if row < 0 or col < 0 or row >= len(A) or col >= len(A[row]) or A[row][col] != 1 :
            return False
        queue.append({'row':row,'col':col,'time':time})
        A[row][col] = 2
        return True


solution  = Solution()

print(solution.solve([[2,1,1],[0,1,1],[1,0,1]]))
print(solution.solve([[2,1,1],[1,1,0],[0,1,1]]))
print(solution.solve([[2,1,1],[1,2,0],[0,1,1]]))