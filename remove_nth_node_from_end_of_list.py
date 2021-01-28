# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None: return None

        curr = head
        length_counter = 0
        while curr:
            curr = curr.next
            length_counter += 1
        index = length_counter - n + 1

        if index == 1:
            return head.next

        begin_head = head
        counter = 1
        curr = head
        while counter<=index-1:
            if counter == index-1:
                curr.next = curr.next.next
            counter += 1
            curr = curr.next

        return begin_head
