# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        dummy = result = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        previous = None
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        while dummy and previous:
            temp1 = dummy.next #4
            temp2 = previous.next
            dummy.next = previous
            dummy.next.next = temp1
            dummy = dummy.next.next
            dummy = temp1
            previous = temp2