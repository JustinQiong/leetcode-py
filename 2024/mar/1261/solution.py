from typing import Optional

from TreeNode import TreeNode

"""
1261. Find Elements in a Contaminated Binary Tree
Depth first search solution:
Recover the tree with dfs algo.
Store the elements of recovered vals into a set.
When calling the find method, return if the target value
is in set or not.
"""
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        st = set()
        def dfs(rt):
            st.add(rt.val)
            if rt.left:
                rt.left.val = 2 * rt.val + 1
                dfs(rt.left)
            if rt.right:
                rt.right.val = 2 * rt.val + 2
                dfs(rt.right)
        dfs(root)
        self.root = root
        self.st = st

    def find(self, target: int) -> bool:
        return target in self.st