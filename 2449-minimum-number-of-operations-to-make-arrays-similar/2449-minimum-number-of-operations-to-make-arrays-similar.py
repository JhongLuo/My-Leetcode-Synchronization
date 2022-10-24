class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        even_nums = list(filter(lambda v: v%2 == 0, nums))
        odd_nums = list(filter(lambda v: v%2 == 1, nums))
        even_target = list(filter(lambda v: v%2 == 0, target))
        odd_target = list(filter(lambda v: v%2 == 1, target))
        
        res = 0
        for i in range(len(even_nums)):
            v = even_nums[i] - even_target[i]
            v = max(v, -v)
            res += v
            
        for i in range(len(odd_nums)):
            v = odd_nums[i] - odd_target[i]
            v = max(v, -v)
            res += v
            
        return res // 4