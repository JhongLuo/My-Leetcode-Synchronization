class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        st = set(nums)
        res = len(st)
        added = set()
        for v in nums:
            new_v = 0
            while v != 0:
                new_v *= 10
                new_v += v % 10
                v //= 10
            if new_v not in st and new_v not in added:
                added.add(new_v)
                res += 1
        return res
            