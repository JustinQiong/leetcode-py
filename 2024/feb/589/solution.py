from typing import List

"""
589. N-ary Tree Preorder Traversal
Depth first search solution
append root.val to res array first and
depth first search each child recursively.
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        def dfs(rt):
            res.append(rt.val)
            for child in rt.children:
                dfs(child)

        dfs(root)

        return res