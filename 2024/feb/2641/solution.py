from typing import Optional

import TreeNode

"""
2641. Cousins in Binary Tree II
Breadth First Search Solution:
Iterate each level of the tree with a list to store the nodes.
Calculate the sum and the left and right node of each parent node.
"""
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        root.val = 0
        while len(q) > 0:
            q2 = []
            sm = 0
            for fa in q:
                if fa.left:
                    q2.append(fa.left)
                    sm += fa.left.val
                if fa.right:
                    q2.append(fa.right)
                    sm += fa.right.val

            for fa in q:
                childSum = (fa.left.val if fa.left else 0) + (fa.right.val if fa.right else 0)
                if fa.left:
                    fa.left.val = sm - childSum

                if fa.right:
                    fa.right.val = sm - childSum

            q = q2

        return root