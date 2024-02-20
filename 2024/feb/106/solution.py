from typing import List, Optional

from TreeNode import TreeNode

"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Map val to index in inorder array to map mp.
Build the tree recursively by pop out the root from postorder array.
With the help of the map mp we can calculate the length of the left 
and right subtrees. And we can divide the postorder array with the tree lengths.
Then build right subtree and left subtree recursively.
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = {val: idx for idx, val in enumerate(inorder)}

        n = len(postorder)

        def build(iL, iR):
            if iL > iR:
                return None

            rt = postorder.pop()
            root = TreeNode(rt)
            mid = mp[rt]
            root.right = build(mid + 1, iR)
            root.left = build(iL, mid - 1)

            return root

        return build(0, n - 1)