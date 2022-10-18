class Solution:
    def maxArea(self, height: List[int]) -> int:
        lef = 0
        rig = len(height) - 1
        res = 0
        while lef < rig:
            res = max(min(height[lef], height[rig]) * (rig - lef), res)
            if height[lef] <= height[rig]:
                old_lef_h = height[lef]
                while lef < rig and height[lef] <= old_lef_h:
                    lef += 1
            else:
                old_rig_h = height[rig]
                while lef < rig and height[rig] <= old_rig_h:
                    rig -= 1
        return res