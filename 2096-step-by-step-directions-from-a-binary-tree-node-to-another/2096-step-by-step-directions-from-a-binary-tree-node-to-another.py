# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        son2father = dict()
        self.startNode = None
        def recur(father, node):
            if node == None:
                return
            else:
                if father != None:
                    son2father[node] = father
                if node.val == startValue:
                    self.startNode = node
                recur(node, node.left)
                recur(node, node.right)
                
                
        recur(None, root)
        queue = [(self.startNode, '')]
        visited = set()
        while len(queue):
            node, path = queue.pop()
            visited.add(node)
            if node.val == destValue:
                return path
            if node.left and node.left not in visited:
                queue.append((node.left, path + 'L'))
            if node.right and node.right not in visited:
                queue.append((node.right, path + 'R'))
            if node in son2father and son2father[node] not in visited:
                queue.append((son2father[node], path + 'U'))
        
                