## sum root to leaf numbers
## https://leetcode.com/problems/sum-root-to-leaf-numbers/
## 20210201

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        if root is None: return 0

        node_lst = [root]
        string_lst = [str(root.val)] ##key
        result_sum = 0

        while len(node_lst) > 0:
            curr_node = node_lst.pop(-1)
            curr_string = string_lst.pop(-1)

            if curr_node.left is None and curr_node.right is None:
                result_sum += int(curr_string)
            if curr_node.right is not None:
                node_lst.append(curr_node.right)
                string_lst.append(curr_string + str(curr_node.right.val))
            if curr_node.left is not None:
                node_lst.append(curr_node.left)
                string_lst.append(curr_string + str(curr_node.left.val))

        return result_sum
