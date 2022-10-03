class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        lower_bound = min(int(n**0.5) + 2, n)
        
        isPrime = [True] * n
        for i in range(0, min(n, 2)):
            isPrime[i] = 0 
        for v in range(2, lower_bound):
            if isPrime[v]:
                for multi in range(v*v, n, v):
                    isPrime[multi] = False
                    
        return sum(isPrime)