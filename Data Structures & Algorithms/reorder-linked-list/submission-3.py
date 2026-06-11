# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        previous = None
        slow.next = None

        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        while previous:
            temp1, temp2 = head.next, previous.next
            head.next = previous
            previous.next = temp1
            head, previous = temp1, temp2
