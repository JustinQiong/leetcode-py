from typing import Optional

import TreeNode

"""
993. Cousins in Binary Tree
Breadth First Search Solution:
Iterate through each level of the nodes in binary tree
with two rolling list. If both of the x and y has been 
found in the child nodes and they have different parents
then x and y are cousins.
"""
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        while len(q) > 0:
            q1 = []
            paX, paY = None, None
            for node in q:
                if node.left:
                    q1.append(node.left)
                    if node.left.val == x:
                        paX = node
                    if node.left.val == y:
                        paY = node

                if node.right:
                    q1.append(node.right)
                    if node.right.val == x:
                        paX = node
                    if node.right.val == y:
                        paY = node
            if (not paX and paY) or (not paY and paX):
                return False

            if paX and paY and paX != paY:
                return True

            q = q1

        return False
