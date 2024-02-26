from typing import Optional

from TreeNode import TreeNode

"""
938. Range Sum of BST
Depth first search solution:
if r.val in range [low, high], sum r.val
"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def dfs(r):
            if not r:
                return

            if r.val > high:
                dfs(r.left)
            elif r.val < low:
                dfs(r.right)
            else:
                nonlocal res
                res += r.val
                dfs(r.left)
                dfs(r.right)

        dfs(root)
        return res