class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            gcd = nums[i]
            for j in range(i, n):
                gcd = math.gcd(gcd, nums[j])
                if gcd % k != 0:
                    break
                if gcd == k:
                    res += 1
        return res
            