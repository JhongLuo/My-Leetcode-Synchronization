class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a < b:
            return self.commonFactors(b, a)
        
        # Max Common Divider
        while b != 0:
            a, b = b, a % b
        
        # Get the number of factors of a
        factor2num = dict()
        factor = 2
        while a != 1:
            if a % factor == 0:
                a /= factor
                if factor not in factor2num:
                    factor2num[factor] = 0
                factor2num[factor] += 1
            else:
                factor += 1
        res = 1
        for k, v in factor2num.items():
            res *= v + 1
        return res
            
            
