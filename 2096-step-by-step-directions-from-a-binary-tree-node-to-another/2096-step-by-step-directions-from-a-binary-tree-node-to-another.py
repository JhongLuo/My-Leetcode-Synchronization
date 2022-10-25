# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if root == None:
            return False, False, ''
        
        start1, dest1, str1 = self.recur(root.left, startValue, destValue)
        # if root.left != None:
        #     print(root.left.val, start1, dest1, str1)
        start2, dest2, str2 = self.recur(root.right, startValue, destValue)
        # if root.right != None:
        #     print(root.right.val, start2, dest2, str2)
        
        if start1 and dest1:
            return start1, dest1, str1
        elif start2 and dest2:
            return start2, dest2, str2
        elif start1 and dest2:
            return start1, dest2, str1 + 'U' + 'R' + str2
        elif start2 and dest1:    
            return start2, dest1, str2 + 'U' + 'L' + str1
        else:
            rtnStart = start1 or start2 or root.val == startValue
            rtnDest = dest1 or dest2 or root.val == destValue
            if start1:
                return rtnStart, rtnDest, str1 + 'U'
            elif start2:
                return rtnStart, rtnDest, str2 + 'U'
            elif dest1:
                return rtnStart, rtnDest, 'L' + str1
            elif dest2:
                return rtnStart, rtnDest, 'R' + str2
            else:
                return rtnStart, rtnDest, ''
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        _, _, s = self.recur(root, startValue, destValue)
        return s