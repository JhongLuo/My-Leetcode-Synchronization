# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # refactor tree to map
        mapper = defaultdict(list)
        def build_map(node):
            def build_sub_map(father, son):
                mapper[father.val].append(son.val)
                mapper[son.val].append(father.val)
                build_map(son)
                
            if node.left != None:
                build_sub_map(node, node.left)
            if node.right != None:
                build_sub_map(node, node.right)
        build_map(root)
        
        # dfs the nodes
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
            
        
                
                
        