class BinarySearch:
    def search(self,array,number):
        l = len(array)
        left = 0
        right = l-1
        while left <= right:
            mid = (right+left)//2
            if number == array[mid]:
                return True
            if number > array[mid]:
                left = mid + 1
            if number < array[mid]:
                right = mid-1
        return False
    
searching = BinarySearch()
found = searching.search([1,2,3,4,5,6,7,8,9],8)
print(found)