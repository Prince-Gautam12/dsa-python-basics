class Solution:
    def party(self, A):
        if (A== 1 or A == 2):
            return A
        return ((self.party(A-1)) % 10003 + ((A-1) * self.party(A-2)) % 10003) % 10003


    def solve(self, A):
        if (A == 1 or A == 2):
            return A
        def calc(A, cache):
            if (cache[A] != None): return cache[A]
            ans = (calc(A-1, cache) % 10003 + ((A-1) * calc(A-2, cache)) % 10003) % 10003
            cache[A] = ans
            return ans
        
        cache=[None]*(A+1)
        cache[1] = 1
        cache[2] = 2
        return calc(A, cache)
    
    def partyTab(self, A):
        if (A == 1 or A == 2):
            return A
        cache = [None]*(A+1)
        cache[1] = 1
        cache[2] = 2
        for i in range(3, A+1):
            ans = ((cache[i - 1]) % 10003 + ((i-1) * cache[i - 2]) % 10003) % 10003
            cache[i] = ans
        return cache[A]
    
    


solution = Solution()
answer = solution.party(3)
print(answer) 

answer = solution.party(10)
print(answer)

answer = solution.solve(60041)
print(answer)