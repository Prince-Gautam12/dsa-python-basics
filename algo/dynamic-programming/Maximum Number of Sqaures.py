import math
class Solution():
    def square(self, A):
        cache = [None] * (A+1)
        def solve(A, cache):
            if (cache[A] != None) : return cache[A]
            sqrt = int(math.sqrt(A))
            if sqrt * sqrt == A : return 1
            minvalue = 1000000
            for i in reversed(range(1, sqrt+1)) :
                ans = solve(A - (i*i), cache) 
                minvalue = min(minvalue, ans)
            cache[A] = minvalue+1
            return cache[A]
        return solve(A, cache)

sol = Solution()
print(sol.square(7845))
print(sol.square(5))
print(sol.square(5))


            
