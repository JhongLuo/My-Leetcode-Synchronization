class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        rank2pos = [i for i in range(n)]
        rank2pos.sort(key=lambda x:nums[x])
                
        target = None
        prefixSum = 0
        total = sum(cost)
        for i in range(n):
            prefixSum += cost[rank2pos[i]]
            if prefixSum >= total - prefixSum:
                target = nums[rank2pos[i]]
                break
        
        return sum(abs(target - nums[i]) * cost[i] for i in range(n))
            
        