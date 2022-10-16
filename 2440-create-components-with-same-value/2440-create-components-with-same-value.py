class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        sum_v = reduce(lambda x,y: x+y, nums)
        max_v = reduce(max, nums)
        
        prime_factors = defaultdict(int)
        factor = 2
        tmp_sum = sum_v
        while tmp_sum != 1:
            if tmp_sum % factor == 0:
                tmp_sum /= factor
                prime_factors[factor] += 1
            else:
                factor += 1
        
        prime_factors = [(v, t) for v, t in prime_factors.items()]
        targets = set()
        def prime2factors(pos, multi):
            if pos == len(prime_factors):
                targets.add(multi)
                return
            else:
                prime, times = prime_factors[pos]
                t = 0
                while t <= times:
                    prime2factors(pos + 1, multi)
                    multi *= prime
                    t += 1
            
        prime2factors(0, 1)
        targets = list(targets)
        targets.sort()
        
        mapper = {v:[] for v in range(len(nums))}
        for src, dst in edges:
            mapper[src].append(dst)
            mapper[dst].append(src)
        
        def group_dfs(father, node, target):
            summa = 0
            for nxt in mapper[node]:
                if nxt != father:
                    b, v = group_dfs(node, nxt, target)
                    if not b:
                        return False, None
                    else:
                        summa += v
            
            if summa + nums[node] == target:
                return True, 0
            elif summa + nums[node] < target:
                return True, summa + nums[node]
            else:
                return False, None
        
        for target in targets:
            b, v = group_dfs(None, 0, target)
            if b == True and v == 0:
                return sum_v // target - 1
        return 0
        
        
            
                    
            
            
        
        
        
    