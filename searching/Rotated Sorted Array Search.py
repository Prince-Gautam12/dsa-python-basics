class Solution:
    # Linear Search
    def search(self, A, B):
        for num in A:
            if num == B:
                return True
        return False
    
    # Binary Search
    def searchBinary(self, A, B):
        l = len(A)
        left = 0
        right = l - 1
        while left <= right:
            mid = (left+right)//2
            if A[mid] == B:
                return mid
            if A[mid] > A[left] :
                if A[left] < B < A[mid]:
                    right = mid - 1
                else : left = mid + 1
            else :
                if A[right] < B > A[mid]:
                    left = mid + 1
                else : right = mid - 1
        return -1

    
solution = Solution()
linSearch = solution.search([4, 5, 6, 7, 8, 0, 1, 2], 5)
print(linSearch)

print("-------------Binary-------------")
binSearch = solution.searchBinary([4, 5, 6, 7, 8, 0, 1, 2], 5)
print(binSearch)

binSearch = solution.searchBinary([4, 5, 6, 7, 8, 0, 1, 2], 44)
print(binSearch)

binSearch = solution.searchBinary([4, 5, 6, 7, 8, 0, 1, 2], 2)
print(binSearch)