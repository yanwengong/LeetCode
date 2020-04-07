## reverse linked list
## https://leetcode.com/problems/reverse-linked-list/

def reverseList(head):
    if head is None: return None

    dummy = None

    pre = dummy
    curr =head


    while curr.next:
        next = curr.next
        curr.next = pre
        pre = curr
        curr = next

    curr.next = pre

    return curr
