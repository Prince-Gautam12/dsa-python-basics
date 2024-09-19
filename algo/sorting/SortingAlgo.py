class SortingAlgo:
    def bubbleSort(self, array):
        l = len(array)
        for bubble in range(0, l):
            for curr in range (bubble + 1, l):
                if array[bubble] > array[curr]:
                    # temp = array[bubble]
                    # array[bubble] =  array[curr]
                    # array[curr] = temp
                    array[bubble], array[curr] = array[curr], array[bubble]
        return array

    def selectionSort(self, array):
        pass

    def insertionSort(self, array):
        pass

    def quickSort(self, array):
        pass

    def mergeSort(self, array):
        def merge(a, b):
            merged = []
            i = 0
            j = 0
            while i < len(a) and j < len(b) :
                if a[i] < b[j] :
                    merged.append(a[i])
                    i+=1
                else:
                    merged.append(b[j])
                    j+=1
            if i >= len(a):
                while j < len(b):
                    merged.append(b[j])
                    j+=1
            
            if j >= len(b):
                while i < len(a):
                    merged.append(a[i])
                    i+=1
            return merged
        
        def mySort(array, left, right):
            if left >= right:
                return[array[left]]
            mid = (left+right)//2
            leftSorted = mySort(array, left, mid)
            rightSorted = mySort(array, mid+1, right)
            merged = merge(leftSorted, rightSorted)
            return merged
        sortedArray = mySort(array, 0, len(array)-1)
        return sortedArray

sort = SortingAlgo()
print(sort.bubbleSort([8,7,3,10,9,2]))
print(sort.mergeSort([8,7,3,10,9,2]))

