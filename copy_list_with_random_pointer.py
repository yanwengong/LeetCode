## copy list with random pointer
## https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""






## below does not work, the last random indecator is not tracible
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None

        curr_head = head
        true_head = curr_head

        while head.next is not None:
            curr_head = head.next
            curr.random = head.random

            head = head.next
            curr = curr.next

        return true_head
