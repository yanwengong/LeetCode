## Binary tree level order traversal
## https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        root_lst = [root]
        new_root = []
        large_lst = []

        while !(all(v is None for v in root_lst)):
            small_lst = []
            new_root = []

            for i in range(len(root_lst)):
                small_lst.append(root_lst[i].val)
                new_root.append(root_lst[i].left)
                new_root.append(root_lst[i].right)

            root_lst = new_root
            large_lst.append(small_lst)

        return large_lst


class Solution2:
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        root_lst = [root]
        new_root = []
        large_lst = []

        # while not all(v is None for v in root_lst): # O(n)
        while len(root_lst) > 0: # O(1)
            small_lst = []
            new_root = []

            for i in range(len(root_lst)):
                if root_lst[i] is not None:
                    small_lst.append(root_lst[i].val)
                    if root_lst[i].left:
                        new_root.append(root_lst[i].left)
                    if root_lst[i].right:
                        new_root.append(root_lst[i].right)

            root_lst = new_root
            large_lst.append(small_lst)

        return large_lst
