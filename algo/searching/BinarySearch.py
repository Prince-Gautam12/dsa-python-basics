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
    
    def decresingSearch(self,array,number):
        l = len(array)
        left = 0
        right = l-1
        while left <= right:
            mid = (right+left)//2
            if number == array[mid]:
                return True
            if number > array[mid]:
                right = mid - 1
            if number < array[mid]:
                left = mid + 1
        return False
    
    def binarySearchRecDEc(self, array, number) :
        l = len(array)
        left = 0
        right = l-1
        def recursion(array, number, left, right):
            if left > right : return False
            mid = (right + left) // 2
            if array[mid] == number : return True
            if (array[mid] > number) : return recursion(array, number, mid + 1, right)
            if (array[mid] < number) : return recursion(array, number, left, mid-1)

        return recursion(array, number, left, right)
    
    def binarySearchRecInc(self, array, number) :
        l = len(array)
        left = 0
        right = l-1
        def recursion(array, number, left, right):
            if left > right : return False
            mid = (right + left) // 2
            if array[mid] == number : return True
            if (array[mid] < number) : return recursion(array, number, mid + 1, right)
            if (array[mid] > number) : return recursion(array, number, left, mid-1)

        return recursion(array, number, left, right)


    
searching = BinarySearch()
found = searching.search([1,2,3,4,5,6,7,8,9],8)
print(found)

found = searching.decresingSearch([9,8,7,6,5,4,3,2,1],7)
print(found)


found = searching.binarySearchRecDEc([9,8,7,6,5,4,3,2,1],7)
print(found)


found = searching.binarySearchRecInc([1,2,3,4,5,6,7,8,9],7)
print(found)