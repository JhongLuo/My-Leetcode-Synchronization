class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        summa = 0
        for i, v in enumerate(nums):
            summa += i * v
        n = len(nums)
        res = summa
        for i in range(n - 1, 0, -1):
            summa = summa + total - nums[i] * n
            res = max(res, summa)
        return res
            
        