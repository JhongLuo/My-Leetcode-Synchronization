class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        summa = 0
        for i, v in enumerate(nums):
            summa += v
            res = max(res, (summa // (i + 1) if summa % (i + 1) == 0 else summa // (i + 1) + 1))
        return res
            
        
        