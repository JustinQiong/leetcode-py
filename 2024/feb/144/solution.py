from typing import Optional, List

import TreeNode

"""
144. Binary Tree Preorder Traversal
Iterate solution:
iterate through the left node of the root to the end
and push the node into a stack. When meet the end of the
left branch, pop out the node from the stack and visit the
right node of the node. Do the iteration again on the right node.
Repeat the action until the stack is empty and node is null.
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        return res