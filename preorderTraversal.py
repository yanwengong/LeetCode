## binary tree preorder traversal
## https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## recursive approach
class Solution:
    def __init__(self):
        self.L = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None: return []


        self.L.append(root.val)
        l = self.preorderTraversal(root.left)
        r = self.preorderTraversal(root.right)

        return self.L


## iterative approach

class Solution_v2:
    def __init__(self):
        self.L = []
        self.L_output = []

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if root is None: return []

        self.L.append(root)

        while len(self.L) > 0:
            self.L_output.append(self.L[-1].val)
            root = self.L.pop(-1)


            if root.right is not None:
                self.L.append(root.right)
            if root.left is not None:
                self.L.append(root.left)


        return self.L_output
