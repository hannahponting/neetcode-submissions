# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        after = ListNode(0, head)
        before = after
        result = before

        while n > 0:
            after = after.next
            n -= 1
        
        while after and after.next:
            after = after.next
            before = before.next
        
        if before.next:
            before.next = before.next.next
        else:
            before.next = None
        return result.next