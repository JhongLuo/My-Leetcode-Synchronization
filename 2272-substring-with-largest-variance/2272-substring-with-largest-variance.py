class Solution:
    def largestVariance(self, s: str) -> int:
        chars = set()
        for c in s:
            chars.add(c)
        chars = list(chars)
        s = list(s)
        n = len(s)
        pos2next = [None for _ in range(n)]
        c2next = dict()
        for i in range(n-1, -1, -1):
            if s[i] in c2next:
                pos2next[i] = c2next[s[i]]
            c2next[s[i]] = i
                
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
                c1_pos = c2next[c1]
                c2_pos = c2next[c2]
                while True:
                    if c1_pos == None and c2_pos == None:
                        break
                    elif c1_pos == None:
                        c = c2
                        c2_pos = pos2next[c2_pos]
                    elif c2_pos == None:
                        c = c1
                        c1_pos = pos2next[c1_pos]
                    else:
                        if c1_pos < c2_pos:
                            c = c1     
                            c1_pos = pos2next[c1_pos]
                        else: 
                            c = c2
                            c2_pos = pos2next[c2_pos]
                            
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
                    max_summa = max(max_summa, summa - (0 if minus_one else 1))
                    

                res = max(res, max_summa)
        return res
                    
                        
                    
    