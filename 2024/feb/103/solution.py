import collections
from typing import Optional, List

import TreeNode

"""
103. Binary Tree Zigzag Level Order Traversal
Breadth first search with a deque on each level
to output the response of that level respectively
decide to append or append to the head by checking
if each level is append from the left or the right.
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = [root]
        left = True
        while q:
            level = collections.deque()
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if left:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(list(level))

            left = not left

        return res