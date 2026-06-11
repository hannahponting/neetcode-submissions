# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        firstNode = dummy = ListNode(val=0, next = head)
        thirdNode = firstNode
        
        while left > 1:
            firstNode = firstNode.next
            left -= 1
        
        while right > 0:
            thirdNode = thirdNode.next
            right -= 1
        
        third = thirdNode.next
        thirdNode.next = None

        second = firstNode.next
        firstNode.next = None

        previous = third
        end = second
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        firstNode.next = previous

        return dummy.next