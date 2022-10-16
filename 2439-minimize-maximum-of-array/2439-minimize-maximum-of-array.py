class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        summa = 0
        length = len(nums)
        for i, v in enumerate(nums):
            summa += v
            if i == length - 1 or nums[i] > nums[i + 1]:
                res = max(res, (summa // (i + 1) 
                           if (summa % (i + 1) == 0) 
                           else (summa // (i + 1) + 1)))
        return res
            
        
        