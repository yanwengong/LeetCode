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

## use dictionary

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None

        true_head = head ## save the original head

        copy_head = Node(head.val)
        dict = {head : copy_head}

        head = head.next
        while head is not None:

            copy_head = Node(head.val)
            dict[head] = copy_head
            head = head.next

        ## second loop to add .next and .random

        for key in dict:
            copy_head = dict[key]
            if key.next is None:
                next_node = None
            else:
                next_node = dict[key.next]

            if key.random is None:
                random_node = None
            else:
                random_node = dict[key.random]


            copy_head.next = next_node
            copy_head.random = random_node
            #dict[key] = copy_head

        return(dict[true_head])






## below does not work, the last random indecator is not tracible
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None

        true_head = Node(head.val, head.next, head.random)
        curr_head = true_head

        while head.next is not None:
            next_node =  Node(head.next.val, head.next.next, head.next.random)
            if head.random is None:
                curr_head.random = None
            else:
                random_node = Node(head.random.val, head.random.next, head.random.random)
                curr_head.random = random_node

            curr_head.next = next_node


            head = head.next
            curr_head = curr_head.next
