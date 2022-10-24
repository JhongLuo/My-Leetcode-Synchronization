class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        rank2pos = [i for i in range(n)]
        rank2pos.sort(key=lambda x:nums[x])
        
        prefixS = [0]
        for i in range(n):
            prefixS.append(cost[rank2pos[i]] + prefixS[-1])
        
        target = None
        for i in range(n):
            if prefixS[i + 1] >= prefixS[-1] - prefixS[i + 1]:
                target = nums[rank2pos[i]]
                break
            
        res = 0
        for i in range(n):
            res += max(target - nums[i], nums[i] - target) * cost[i]
        return res
            
        