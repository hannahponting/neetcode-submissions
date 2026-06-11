# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = head = ListNode()
        carry = False

        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val 
                if carry:
                    total = total +1
                    carry = False
                if total > 9:
                    total -= 10
                    carry = True
                new.next = ListNode(total)
                new = new.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total = l1.val
                if carry:
                    total = total +1
                    carry = False
                if total > 9:
                    total -= 10
                    carry = True
                new.next = ListNode(total)
                new = new.next
                l1 = l1.next
            elif l2:
                total = l2.val
                if carry:
                    total = total +1
                    carry = False
                if total > 9:
                    total -= 10
                    carry = True
                new.next = ListNode(total)
                new = new.next
                l2 = l2.next
        if carry:
            new.next = ListNode(1)
            new = new.next
        return head.next