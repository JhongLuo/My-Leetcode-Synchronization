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
            res += abs(even_nums[i] - even_target[i])            
        for i in range(len(odd_nums)):
            res += abs(odd_nums[i] - odd_target[i])
        return res // 4