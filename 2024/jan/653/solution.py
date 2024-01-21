from typing import Optional

from TreeNode import TreeNode

"""
653. Two Sum IV - Input is a BST
Depth First Search Solution:
Use a set to store the values of the node visited.
If k - val in set, return True.
Else depth first search the left and right subtrees.
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(rt):
            if not rt:
                return False

            if k - rt.val in st:
                return True
            else:
                st.add(rt.val)
                return dfs(rt.left) or dfs(rt.right)

        st = set()

        return dfs(root)
