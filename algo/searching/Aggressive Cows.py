class Solution:
    def cowProblem(self, A, cows):
        A.sort()
        left = 1
        right = max(A) - min(A)
        ans = 1
        while left <= right:
            mid = (left + right) // 2
            if self.checkMidPossibility(mid, cows, A) :
                if mid > ans : 
                    ans = mid
                left = mid +1
            else :
                right = mid - 1
        return ans

    def checkMidPossibility(self, mid, cows, A) :
        cowplaced = 1
        lastPos = A[0]
        for i in range(1, len(A)):
            currpos = A[i]
            if mid + lastPos <= currpos:
                cowplaced+=1
                lastPos = currpos
            
            if cowplaced == cows:
                return True
        return False
    

solution = Solution()
answer = solution.cowProblem( [1, 2, 3, 4, 5], 3)
print(answer)