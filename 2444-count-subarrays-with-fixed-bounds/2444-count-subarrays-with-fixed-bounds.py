class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lefBound = -1
        minKPos = None
        maxKPos = None
        res = 0
        for i, v in enumerate(nums):
            if v == minK:
                minKPos = i
            if v == maxK:
                maxKPos = i
            if v < minK or v > maxK:
                lefBound = i
                minKPos = None
                maxKPos = None
                
            if minKPos != None and maxKPos != None:
                res += min(minKPos, maxKPos) - lefBound
                
        return res
                
            
                
        
            
            
        
        
                