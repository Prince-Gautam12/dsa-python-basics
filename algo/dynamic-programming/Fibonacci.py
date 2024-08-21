class Fibonacci: 
    # TC: O(2^n)    SC: O(h) 
    def calculate(self, n):
        if (n == 0 or n == 1) : return n
        return self.calculate(n-1) + self.calculate(n-2)

    # TC: O(n)    SC: O(2n)
    def calculateDp(self, n):
        def calc(n, cache):
            if (cache[n] != None): return cache[n]
            ans = calc(n-1, cache) + calc(n-2, cache)
            cache[n] = ans
            return ans
        
        cache= [None]*(n+1)
        cache[0] = 0
        cache[1] = 1
        return calc(n, cache)
    # SC : O(n)   TC: O(N)
    def calculateIterative(self, n) :
        cache = [None]*(n+1)
        cache[0] = 0
        cache[1] = 1
        for i in range(2, n+1):
            ans = cache[i-1] + cache[i-2]
            cache[i] = ans
        return cache[n]
    
    # TC : O(N) SC: O(1)
    def calculateBest(self, n) :
        if (n == 0 or n ==1): return n
        n_2 = 0
        n_1 = 1
        for i in range(2, n+1):
            ans =  n_1+ n_2
            n_2 = n_1
            n_1 = ans
        return n_1

        
fibonacci = Fibonacci()
print(fibonacci.calculateDp(50))
print(fibonacci.calculateDp(40))
print(fibonacci.calculateDp(30))

print("------------------------- Iterative -------------------------------")

print(fibonacci.calculateIterative(50))
print(fibonacci.calculateIterative(40))
print(fibonacci.calculateIterative(30))


print("------------------------- Iterative Best-------------------------------")

print(fibonacci.calculateBest(50))
print(fibonacci.calculateBest(40))
print(fibonacci.calculateBest(30))