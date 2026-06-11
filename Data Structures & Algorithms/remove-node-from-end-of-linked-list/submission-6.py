# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0, head)

        end = result
        first = result

        while n > -1:
            end = end.next
            n -= 1
        
        while end:
            end = end.next
            first = first.next

        first.next = first.next.next
        return result.next