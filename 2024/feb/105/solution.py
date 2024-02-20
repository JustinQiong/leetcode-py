from typing import List, Optional

import TreeNode

"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Map the index of each node in inorder traversal array.
Find the first element of preorder traversal array to build the root.
Recursively build left and right subtree with the subarray of inorder 
and preorder traversal array.
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i, num in enumerate(inorder):
            mp[num] = i

        n = len(preorder)

        def build(pre, preIndex, io, iL, iR):
            if preIndex > n - 1 or iL > iR:
                return None

            rt = pre[preIndex]
            root = TreeNode(rt)
            mid = mp[rt]
            lenLeft = mid - iL
            root.left = build(pre, preIndex + 1, io, iL, mid - 1)
            root.right = build(pre, preIndex + lenLeft + 1, io, mid + 1, iR)

            return root

        return build(preorder, 0, inorder, 0, n - 1)