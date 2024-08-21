class Solution:
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        
        low = 1
        high = A
        
        while low <= high:

            mid = (low + high) // 2
            
            calc = mid * mid

            if calc == A:
                return mid
            
            elif calc < A:
                low = mid +1

            else:
                high = mid - 1

        return high

    
solution = Solution()
answer = solution.sqrt(10)
print(answer)

answer = solution.sqrt(25)
print(answer)