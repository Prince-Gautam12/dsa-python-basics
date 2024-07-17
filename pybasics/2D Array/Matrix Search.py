class Solution:
    #  O(NxM)
    def searchMatrix(self, A, B):
        for i in range(0, len(A)) :
            for j in range(0, len(A[i])) :
                if A[i][j] == B : 
                    return 1

        return 0
    # O(Nlog(M))
    def searchBinary(self, A, B):
        for array in A :
            l = 0
            r = len(array)-1
            while (l<=r) :
                mid = (l+r)//2
                if (array[mid] == B) : return 1
                if (array[mid] < B) : l = mid+1
                else : r = mid - 1
        return 0
    
    # O(logN x logM)
    def optimalSolution(self, A, B) :
        l = 0 
        r = len(A) - 1
        while (l <= r) :
            mid = (l + r)//2
            array = A[mid]
            if (array[0] <= B):
                la = 0
                ra = len(array)-1
                while (la<=ra) :
                    midA = (la+ra)//2
                    if (array[midA] == B) : return 1
                    if (array[midA] < B) : la = midA+1
                    else : ra = midA - 1
                l = mid + 1
            else :
                r = mid - 1
        return 0
            


    
solution = Solution()
search = solution.optimalSolution([
  [3],
  [29],
  [36],
  [63],
  [67],
  [72],
  [74],
  [78],
  [85]
], 41)
print(search)