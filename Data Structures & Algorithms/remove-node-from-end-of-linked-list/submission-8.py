# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        before = after = node = ListNode(0, head)
        
        while n and after:
            after = after.next
            n -= 1
        
        while after and after.next:
            before = before.next
            after = after.next

        if before.next:
            before.next = before.next.next
        else:
            before.next = None
        return node.next
