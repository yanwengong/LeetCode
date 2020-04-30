## Path sum
## https://leetcode.com/problems/path-sum/
## binary tree, traveral



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkLeaf(self, root):
            if root.left == root.right == None:
                return True

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:


        ## corner case
        #if root.val > sum: return False

        if root is None: return False

        if root.val == sum and self.checkLeaf(root):
            return True

        x = self.hasPathSum(root.left, sum - root.val)
        y = self.hasPathSum(root.right, sum - root.val)

        if x == True or y == True:
            return True
        else:
            return False
