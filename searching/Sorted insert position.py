class Solution:
    def searchInsert(self, A, B):
        for i in range(0,len(A)):
            # print(f"Comparing : {B}  >=  {A[i]}" )
            if A[i] >= B:
                # print(f"Found position {i}")
                return i
        # print(f"out of array  {i}")
        return i + 1
    
    def searchInsertBinary(self, A, B):
        l = len(A)
        left = 0
        right = l-1
        #if A[0] > B : return 0
        while left < right:
            mid = (right+left)//2
            if B == A[mid]:
                return mid
            if B > A[mid]:
                left = mid + 1
            if B < A[mid]:
                right = mid
        #print(f"mid : {mid}")
        return  right + 1 if  A[right] < B else right 

solution  = Solution()
print("---------------For LinearSearch-----------------")
searchIdx  = solution.searchInsert([1, 3, 5, 6], 5)
print(searchIdx)

searchIdx  = solution.searchInsert([1, 3, 5, 6], 7)
print(searchIdx)

searchIdx  = solution.searchInsert([1, 3, 5, 6], 2)
print(searchIdx)

searchIdx  = solution.searchInsert([1, 3, 5, 6], 0)
print(searchIdx)

print("----------------For BinarySearch------------------")
searchIdxBinary = solution.searchInsertBinary([1, 3, 5, 6], 5)
print(searchIdxBinary)

searchIdxBinary = solution.searchInsertBinary([1, 3, 5, 6], 7)
print(searchIdxBinary)

searchIdxBinary = solution.searchInsertBinary([1, 3, 5, 6], 2)
print(searchIdxBinary)

searchIdxBinary = solution.searchInsertBinary([1, 3, 5, 6], 0)
print(searchIdxBinary)