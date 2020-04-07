## in order tree traversal without recursion
## https://leetcode.com/problems/binary-tree-inorder-traversal/
## https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.L = []
        self.L_output = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None: return []

        curr = root
        while True:
            if curr is not None:
                self.L.append(curr)
                curr = curr.left

            elif len(self.L) > 0:
                curr = self.L[-1]
                self.L_output.append(self.L[-1].val)
                self.L.pop(-1)
                curr = curr.right

            else:
                return(self.L_output)
