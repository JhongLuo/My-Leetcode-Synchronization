class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:   
        @cache
        def powerfor2(idx):
            if idx == 0:
                return 1
            elif idx == 1:
                return 2
            else:
                return (powerfor2(idx // 2) * powerfor2(idx - idx // 2)) % 1000000007

        @cache
        def find_less(n):
            if n == 1:
                return 0
            else:
                return 1 + find_less(n // 2)
            
        powers = []
        while n != 0:
            powers.append(find_less(n))
            n -= powerfor2(powers[-1])
        powers.sort()
        
        prefixS = [0]
        for v in powers:
            prefixS.append(v + prefixS[-1])
        
        res = []
        for left, right in queries:
            res.append(powerfor2(prefixS[right + 1] - prefixS[left]))
        return res
            
        
        
        
        