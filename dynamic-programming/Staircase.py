class Solution:
    def climbStairs(self, A):
        if (A== 1 or A == 2):
            return A
        return (self.climbStairs(A-1) % 1000000007  + self.climbStairs(A-2) % 1000000007) % 1000000007


    def climbStairsdp(self, A):
        if (A == 1 or A == 2):
            return A
        def calc(A, cache):
            if (cache[A] != None): return cache[A]
            ans = calc(A-1, cache) + calc(A-2, cache)
            cache[A] = ans
            return ans
        
        cache=[None]*(A+1)
        cache[1] = 1
        cache[2] = 2
        return calc(A, cache)


    def climbStairsTab(self, A):
        if (A == 1 or A == 2):
            return A
        cache = [None]*(A+1)
        cache[1] = 1
        cache[2] = 2
        for i in range(3, A+1):
            ans = cache[i-1] + cache[i-2]
            cache[i] = ans
        return cache[A]
    
    def climbStairsBest(self, A):
        if (A == 1 or A == 2):
            return A
        A_2 = 1
        A_1 = 2
        for i in range(3, A+1):
            ans =  (A_1 + A_2) % 1000000007
            A_2 = A_1
            A_1 = ans
        return A_1


find = Solution()
answer = find.climbStairsdp(4)
print(answer)

answer = find.climbStairsdp(4)
print(answer)

find = Solution()
answer = find.climbStairsTab(4)
print(answer)

find = Solution()
answer = find.climbStairsBest(55007)
print(answer)