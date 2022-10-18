class Solution:        
    @cache
    @staticmethod
    def recur(n):
        if n == 1:
            return -1
        elif n == 2:
            return -2
        elif n == 3:
            return -6
        elif n == 4:
            return -5
        else:
            print(n - 4, Solution.recur(n - 4))
            print(n, - (n * (n - 1) // (n - 2)) + (n - 3) + Solution.recur(n - 4))
            return - (n * (n - 1) // (n - 2)) + (n - 3) + Solution.recur(n - 4)
        
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        else:
            return 2 * (n * (n - 1) // (n - 2)) + Solution.recur(n)
        
            