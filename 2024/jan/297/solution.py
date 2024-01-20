from collections import deque

from TreeNode import TreeNode

"""
297. Serialize and Deserialize Binary Tree
Breadth First Search Solution:
Use a queue to line up the node of each level of the 
Binary Tree.
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"

        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")

        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return

        li = data[1:-1].split(",")

        queue = deque()
        root = TreeNode(int(li[0]))
        queue.append(root)
        i = 1
        while queue:
            node = queue.popleft()
            if li[i] != "null":
                node.left = TreeNode(int(li[i]))
                queue.append(node.left)
            i += 1

            if li[i] != "null":
                node.right = TreeNode(int(li[i]))
                queue.append(node.right)
            i += 1

        return root
