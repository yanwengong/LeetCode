## find the middle of the linked ListNode
## https://leetcode.com/problems/middle-of-the-linked-list/description/

def middleNode(head):
    fast = head
    slow = head

    if head.next is None:
        return head

    while True:

        fast = fast.next.next

        slow = slow.next

        if fast is None:
            return slow
        elif fast.next == None:
            return slow
