from collections import deque
class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        def convertToListOfStrings(input_list_of_lists):
            A[:] = [''.join(row) for row in input_list_of_lists]
        def convertToListOfLists(input_list):
            A[:] =  [list(row) for row in input_list]
        convertToListOfLists(A)
        def addNeighbor(row, col, set, queue, A):
            tup = (row, col)
            if row < 0 or row >= len(A) or col < 0 or col >= len(A[row]) or A[row][col] == 'X' or tup in set: return
            set.add(tup)
            queue.append(tup)
        s = set()
        queue = deque()
        self.iterateBoundaryForZero(A, s, queue)
        while len(queue) > 0:
            curr = queue.popleft()
            row, col = curr[0], curr[1]
            addNeighbor(row-1, col, s, queue, A)
            addNeighbor(row+1, col, s, queue, A)
            addNeighbor(row, col-1, s, queue, A)
            addNeighbor(row, col+1, s, queue, A)
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                tup = (i,j)
                if A[i][j] == 'O' and  tup not in s:
                    A[i][j] = 'X'
        convertToListOfStrings(A)

    def iterateBoundaryForZero(self, A, s, queue):
        rows, cols = len(A), len(A[0])
        
        for row in range(rows):
            firstCol, lastCol = 0, cols - 1 
            tupFirstCol, tupLastCol = (row, firstCol), (row, lastCol)
            if A[row][firstCol] == 'O' and tupFirstCol not in s:
                queue.append(tupFirstCol)
                s.add(tupFirstCol)

            if A[row][lastCol] == 'O' and tupLastCol not in s:
                queue.append(tupLastCol)
                s.add(tupLastCol)
        
        for col in range(cols):
            firstRow, lastRow = 0, rows-1
            tupFirstRow, tupLastRow = (firstRow, col), (lastRow, col)
            if A[firstRow][col] == 'O' and tupFirstRow not in s:
                queue.append(tupFirstRow)
                s.add(tupFirstRow)
            if A[lastRow][col] == 'O' and tupLastRow not in s:
                queue.append(tupLastRow)
                s.add(tupLastRow)
        


sol = Solution()
# print(sol.solve([ 
#        ['X', 'X', 'X', 'X'],
#        ['X', 'O', 'O', 'X'],
#        ['O', 'X', 'O', 'X'],
#        ['X', 'O', 'O', 'O'] 
#      ]))

print(sol.solve(["XXXX","XOOX","OXOX","XOXO"]))