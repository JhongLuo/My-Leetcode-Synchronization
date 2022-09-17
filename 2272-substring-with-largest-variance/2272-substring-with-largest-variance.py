class Solution:
    def largestVariance(self, s: str) -> int:
        chars = set()
        for c in s:
            chars.add(c)
        chars = list(chars)
        
        if len(chars) <= 1:
            return 0
        res = 0
        for c1 in chars:
            for c2 in chars:
                if c2 == c1:
                    continue
                summa, max_summa = 0, 0
                minus_one = False
                minus_one_when_max = False
                for i, c in enumerate(s):
                    if c == c1:
                        if summa < 0:
                            summa = 1
                            minus_one = False
                        else:
                            summa += 1
                    elif c == c2:
                        if summa < 0:
                            summa = -1
                            minus_one = True
                        else:
                            summa -= 1
                            minus_one = True
                    else:
                        continue
                    
                    max_summa = max(max_summa, summa - (0 if minus_one else 1))
                        
                res = max(res, max_summa)
        return res
                    
                        
                    
    