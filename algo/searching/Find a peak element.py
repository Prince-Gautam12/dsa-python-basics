class Solution:
    # linear Search
    def findPeakElement(self, A):
        l = len(A)
        
        for i in range(1, l-1):
            if A[i] >= A[i - 1] and A[i] >= A[i + 1]:
                return A[i]
            
        if A[0] >= A[1] : return A[0]
        if A[l-1] >= A[l-2] : return A[l-1]
    
    # Binary Search
    def peakElementBinary(self, A):
        l = len(A)
        left = 0 
        right = l-1
        while (right >= left):
            mid = (right+left)//2
            if( (mid == l-1 or A[mid] >= A[mid+1] ) and (mid == 0 or A[mid] >= A[mid-1] )) :
                return A[mid]
            elif (mid < l-1 and A[mid] < A[mid+1]) :
                left = mid+1
            elif (mid > 0 and A[mid] < A[mid-1]) :
                right = mid-1
        pass
        

solution = Solution()
find = solution.findPeakElement([5,7,100,12])
print(find)
find = solution.findPeakElement([23, 7, 35, 32, 10, 19, 4, 55, 28, 3, 41, 8, 36, 12, 27, 15, 50, 21, 5, 34])
print(find)

print("------------------Binary Search-------------------")

findBin = solution.peakElementBinary([5,4])
print(findBin)

findBin = solution.peakElementBinary([5,7,100,12])
print(findBin)

findBin = solution.peakElementBinary([23, 7, 35, 32, 10, 19, 4, 55, 28, 3, 41, 8, 36, 12, 27, 15, 50, 21, 5, 34])
print(findBin)