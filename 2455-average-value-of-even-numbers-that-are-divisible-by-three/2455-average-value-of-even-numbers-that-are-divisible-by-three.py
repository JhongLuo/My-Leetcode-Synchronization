class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for v in nums:
            if v % 2 == 0 and v % 3 == 0:
                total += v
                count += 1
        if count == 0:
            return 0
        else:
            return total // count
    