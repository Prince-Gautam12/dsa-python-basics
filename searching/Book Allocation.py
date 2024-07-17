class Solution:
    def bookProblem(self, books, students):
        if (books == None or len(books) < students) : return -1
        minPages = max(books)
        maxPages = sum(books)
        ans =  maxPages
        while minPages <= maxPages:
            midPages = (minPages + maxPages) // 2
            if self.checkpossibility(midPages, students, books):
                maxPages = midPages -1
                ans = midPages
            else:
                minPages = midPages+1

        return ans
    
    def checkpossibility(self, maxAllowedPages, students, books):
        completedBook = 0

        while (students > 0):
            allocatePages = 0
            for i in range(completedBook, len(books)):
                pages = books[i]
                if maxAllowedPages < allocatePages + pages:
                    break
                allocatePages += pages
                completedBook+=1
            students-=1

        return students == 0 and completedBook == len(books)
    
solution = Solution()
print(solution.bookProblem([12,34,67,90], 2))
print(solution.bookProblem([31,14,19,75], 12))
