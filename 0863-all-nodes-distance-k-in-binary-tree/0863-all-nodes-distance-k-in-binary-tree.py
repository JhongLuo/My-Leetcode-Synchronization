# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mapper = defaultdict(list)
        def build_map(node):
            if node.left != None:
                mapper[node.val].append(node.left.val)
                mapper[node.left.val].append(node.val)
                build_map(node.left)
            if node.right != None:
                mapper[node.val].append(node.right.val)
                mapper[node.right.val].append(node.val)
                build_map(node.right)
        build_map(root)
        
        res = list()
        def recur(father_v, node_v, distance):
            if distance == k:
                res.append(node_v)
            else:
                for nxt in mapper[node_v]:
                    if nxt != father_v:
                        recur(node_v, nxt, distance + 1)
        
        recur(None, target.val, 0)
        return res
            
        
                
                
        