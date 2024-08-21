# Q: Find a number in an array
class Searching:
    # def linearSearch(self,number,array):
    #     l =len(array)
    #     for i in range(0,l):
    #         if number == array[i]:
    #             return True
    #     return False
    def linearSearch(self,number,array):
        for num in array:
            if number == num:
                return True
        return False

searching = Searching()
arr =  [1,2,3,4,5,6,7,8,9]
found=searching.linearSearch(4,arr)
print(found)

found=searching.linearSearch(18,arr)
print(found)