class Solution :
    def Recursion(self, A, B) :
        l = len(A)
        left = 0 
        right = l-1
        def recursion(A, B, left, right):
            if left >= right:  
                return right + 1 if A[right] < B else right
            mid = (right + left) // 2
            if A[mid] == B:
                return mid
            elif B > A[mid]:                                                    
                return recursion(A, B, mid+1, right)
            elif B < A[mid]:
                return recursion(A, B, left, mid-1)
        
           
        return recursion(A, B, left, right)

solution  = Solution()

searchIdx  = solution.Recursion([1, 3, 5, 6], 5)
print(searchIdx)

searchIdx  = solution.Recursion([1, 3, 5, 6], 7)
print(searchIdx)

searchIdx  = solution.Recursion([1, 3, 5, 6], 2)
print(searchIdx)

searchIdx  = solution.Recursion([1, 3, 5, 6], 0)
print(searchIdx)