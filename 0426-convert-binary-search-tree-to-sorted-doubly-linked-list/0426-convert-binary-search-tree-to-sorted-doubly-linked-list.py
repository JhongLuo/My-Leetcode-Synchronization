"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def buildDoubleList(node):
            if node.left != None:
                lhead, ltail = buildDoubleList(node.left)
                ltail.right = node
                node.left = ltail
                ltail = node
            else:
                lhead, ltail = node, node

            if node.right != None:
                rhead, rtail = buildDoubleList(node.right)
                ltail.right = rhead
                rhead.left = ltail
            else:
                rtail = ltail
                
            return lhead, rtail
        
        if root == None:
            return None
        head, tail = buildDoubleList(root)
        head.left = tail
        tail.right = head
        return head
                
        