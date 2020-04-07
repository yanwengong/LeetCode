## delete node in a linked list
## Remove all elements from a linked list of integers that have value val.
## https://leetcode.com/problems/remove-linked-list-elements/

def deleteNode(head, val):

    ## special case: delete the first

    if head.val == val:
        head = head.next
    else:
        x = head
        y = head.next
        while y is not None:
            if y.val == val:
                x.next = y.next
            else:
                x = x.next
                y = y.next
    return head


################## Ch's update


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # if head is None:
        #     return None

        if head.val == val:
            head = head.next
        else:
            x = head
            y = head.next
            while y is not None:
                if y.val == val:
                    x.next = y.next
                    # x = x.next
                    # if x is None:
                    #     y = None
                    # else:
                    #     y = x.next
                else:
                    x = x.next
                    y = y.next
        return head


## final Yanwen ###

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        while head.val == val:
            head = head.next
            if head is None:
                return None

        x = head
        y = head.next


        while y:
            if y.val == val:
                x.next = y.next
                y = y.next
                #if x is None:
                #    y = None
                #else:
                #    y = x.next
            else:
                x = x.next
                y = y.next
        return head



####### final Ch ############

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None: return None

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next
