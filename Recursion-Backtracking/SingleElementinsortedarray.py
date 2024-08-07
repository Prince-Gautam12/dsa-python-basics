class Solution():
    def solveBs(self, A):
        l = len(A)
        left = 0
        right = l - 1
        if l == 1:
            return A[0]
        if A[0] != A[1]: 
            return A[0]
        if A[l-1] != A[l-2]:
            return A[l-1]
        
        def recursion(self, A, left, right):
            if left >= right:
                return A[left]
            mid = (left + right) // 2
            
            
            
            
            if mid % 2 == 0:
                 if A[mid] == A[mid+1]:
                     return recursion(A, mid+1, right)
                 else:
                     return recursion(A, left, mid - 1)
                 
            else:
                if A[mid] == A[mid-1]:
                    return recursion(A, mid+1, right)

                else:
                    return recursion(A, left, mid+1)

        return (A, left, right) 

solution = Solution()
search = solution.solveBs([2,2,3,3,4,5,5,6,6,7,7])
print(search)

search = solution.solveBs([2,3,3,4,4,5,5,6,6,7,7])
print(search)

search = solution.solveBs([2,2,3,3,4,4,5,5,6,6,7])
print(search)

search = solution.solveBs([13,13,21,21,27,50,50,102,102,108,108,110,110,117,117,120,120,123,123,124,124,132,132,164,164,166,166,190,190,200,200,212,212,217,217,225,225,238,238,261,261,276,276,347,347,348,348,386,386,394,394,405,405,426,426,435,435,474,474,493,493])
print(search)