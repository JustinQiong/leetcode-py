from typing import Optional, List

import TreeNode

"""
107. Binary Tree Level Order Traversal II
Breadth first solution and then reverse
the res
"""
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = [root]

        while q:
            n = len(q)
            cur = []
            for i in range(n):
                node = q.pop(0)
                cur.append(node.val)
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(cur)

        return res[::-1]