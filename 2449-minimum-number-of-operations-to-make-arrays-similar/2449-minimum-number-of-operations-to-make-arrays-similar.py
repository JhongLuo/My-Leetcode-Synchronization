class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        even_nums = filter(lambda v: v%2 == 0, nums)
        odd_nums = filter(lambda v: v%2 == 1, nums)
        even_target = filter(lambda v: v%2 == 0, target)
        odd_target = filter(lambda v: v%2 == 1, target)
        
        res = 0
        for a, b in zip(even_nums, even_target):
            res += abs(a - b)            
        for a, b in zip(odd_nums, odd_target):
            res += abs(a - b)
        return res // 4