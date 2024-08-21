class Solution:
    def paint(self, A, B, C):
        low = max(C)
        high = sum(C) * len(C)
        ans = 0
        while low <= high :
            mid = (low + high) // 2
            if self.checkTimePossibility(mid, A, C):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1
        ans = ans % 10000003
        return (ans * B)% 10000003
    
    def checkTimePossibility(self, maxTime, A, C):
        painters = 1 
        timeConsumed = 0
        for eachBoardTime in C:
            timeConsumed += eachBoardTime
            if timeConsumed > maxTime:
                painters += 1
                timeConsumed = eachBoardTime
                if painters > A:
                    return False
        return True
    
solution =  Solution()
answer = solution.paint(2, 5, [1, 10])
print(answer)
answer1 = solution.paint(4, 10,[884,228,442,889])
print(answer1)