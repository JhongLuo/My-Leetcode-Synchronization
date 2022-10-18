class Solution:        
    @cache
    @staticmethod
    def recur(n):
        if n > 4:
            return - (n * (n - 1) // (n - 2)) + (n - 3) + Solution.recur(n - 4)
        elif n == 1:
            return -1
        elif n == 2:
            return -2
        elif n == 3:
            return -6
        elif n == 4:
            return -5
            
        
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        else:
            return 2 * (n * (n - 1) // (n - 2)) + Solution.recur(n)
        
            