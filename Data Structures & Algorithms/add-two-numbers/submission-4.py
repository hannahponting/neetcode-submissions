# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        response = ListNode(0)
        dummy = response

        while l1 or l2 or carry:
            list1 = l1.val if l1 else 0
            list2 = l2.val if l2 else 0
            total = carry+ list1+list2
            carry = total // 10
            total = total % 10
            response.next = ListNode(total)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            response = response.next
        
        return dummy.next

