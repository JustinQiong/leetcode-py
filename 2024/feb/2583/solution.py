from typing import Optional

from TreeNode import TreeNode

"""
2583. Kth Largest Sum in a Binary Tree
Record the level sum with breadth first search in an array, 
and find the kth largest level sum in the array.
"""


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        pq = []

        q = [root]
        while q:
            nodes = q
            q = []
            level = 0
            for node in nodes:
                level += node.val
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            pq.append(level)

        if len(pq) < k:
            return -1
        else:
            pq.sort()
            return pq[-k]
