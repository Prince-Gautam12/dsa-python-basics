class Solution:
    # @param A : list of integers
    # @return an integer
    # O(N)
    def solve(self, A):
        l = len(A)
        for i in range(0,l):
            if (i>0 and A[i] == A[i-1]) or (i<l-1 and A[i] == A[i+1]):
                i = i+1
            else:
                return A[i]
            
    def solveXor(self, A):
        ans = 0
        for num in A :
            ans = ans^num
        return ans
            
    # O(logN)
    def solveBs(self, A): 
        l = len(A)
        left = 0
        right = l-1
        if l == 1:
            return A[0]
        if A[0] != A[1]: 
            return A[0]
        if A[l-1] != A[l-2]:
            return A[l-1] 
        while left < right:
            mid = (right + left)//2
            if mid%2 == 0:
                if A[mid] == A[mid+1]:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                if A[mid] == A[mid-1]:
                    left = mid + 1
                else:
                    right = mid
        return A[left]




solution = Solution()
search = solution.solve([2,2,3,3,4,4,5,5,6,6,7])
print(search)

search = solution.solveBs([2,2,3,3,4,5,5,6,6,7,7])
print(search)

search = solution.solveBs([2,3,3,4,4,5,5,6,6,7,7])
print(search)

search = solution.solveBs([2,2,3,3,4,4,5,5,6,6,7])
print(search)

search = solution.solveBs([13,13,21,21,27,50,50,102,102,108,108,110,110,117,117,120,120,123,123,124,124,132,132,164,164,166,166,190,190,200,200,212,212,217,217,225,225,238,238,261,261,276,276,347,347,348,348,386,386,394,394,405,405,426,426,435,435,474,474,493,493])
print(search)

print("----------------- XOR -----------------")
search = solution.solveXor([2,2,3,3,4,4,5,5,6,6,7])
print(search)

search = solution.solveXor([2,2,3,3,4,5,5,6,6,7,7])
print(search)

search = solution.solveXor([2,3,3,4,4,5,5,6,6,7,7])
print(search)

search = solution.solveXor([2,2,3,3,4,4,5,5,6,6,7])
print(search)

search = solution.solveXor([13,13,21,21,27,50,50,102,102,108,108,110,110,117,117,120,120,123,123,124,124,132,132,164,164,166,166,190,190,200,200,212,212,217,217,225,225,238,238,261,261,276,276,347,347,348,348,386,386,394,394,405,405,426,426,435,435,474,474,493,493])
print(search)