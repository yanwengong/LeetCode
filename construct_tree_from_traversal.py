## construct binary tree from preorder and inorder Traversal
## https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, list, val):
        for i in range(len(list)):
            if list[i] == val:
                return(i)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(preorder) == 0: return None

        rootval = preorder[0]
        root = TreeNode(rootval)
        rootval_idx = self.find(inorder, rootval)
        left_inorder = inorder[:rootval_idx]
        right_inorder = inorder[rootval_idx + 1:]


        left_inorder_len = len(left_inorder)
        left_preorder = preorder[1: left_inorder_len + 1]
        right_preorder = preorder[left_inorder_len + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
