class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        sum_v = reduce(lambda x,y: x+y, nums)
        max_v = reduce(max, nums)
        
        factors = []
        factor = 2
        tmp_sum = sum_v
        while tmp_sum != 1:
            if tmp_sum % factor == 0:
                tmp_sum /= factor
                factors.append(factor)
            else:
                factor += 1
        
        targets = {1}
        
        import itertools
        for l in range(len(factors)):
            for subset in itertools.combinations(factors, l):
                multi = 1
                for v in subset:
                    multi *= v
                if multi >= max_v:
                    targets.add(multi)
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
        
