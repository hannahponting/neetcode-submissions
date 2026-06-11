# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = head, head.next

        # find middle
        while second and second.next:
            first = first.next
            second = second.next.next
        
        end = first.next
        first.next = previous = None
        
        # reverse end
        while end:
            temp = end.next
            end.next = previous
            previous = end
            end = temp

        dummy = previous
        while previous:
            temp1 = head.next
            temp2 = previous.next
            head.next = previous
            previous.next = temp1
            head = temp1
            previous = temp2
        
