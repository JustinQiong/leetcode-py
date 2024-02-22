from typing import List, Optional

from TreeNode import TreeNode

"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Map postorder traversal from number to index.
With the help of preorder traversal array and the postorder map.
We can calculate the length of left subtree. Then we can divide
postorder array and preorder array into left and right partitions 
with the left subtree length.Then recursively build the subtree with 
the same logic.
"""
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postmp = {n: i for i, n in enumerate(postorder)}

        def build(preLeft, preRight, postLeft, postRight):
            if preLeft > preRight:
                return None

            leftLen = 0
            if preLeft < preRight:
                leftLen = postmp[preorder[preLeft + 1]] - postLeft + 1

            return TreeNode(preorder[preLeft],
                            build(preLeft + 1, preLeft + leftLen, postLeft, postLeft + leftLen - 1),
                            build(preLeft + leftLen + 1, preRight, postLeft + leftLen, postRight - 1))

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)