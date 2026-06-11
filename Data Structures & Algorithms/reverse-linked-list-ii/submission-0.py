# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        rightList = head
        dummy = ListNode(0, head)
        leftList = dummy

        while left > 1:
            leftList = leftList.next
            rightList = rightList.next
            left -= 1
            right -= 1
        while right > 1:
            rightList = rightList.next
            right -= 1
        
        current = middle = leftList.next
        leftList.next = None
        end = rightList.next
        rightList.next = None

        previous = None
        while middle:
            temp = middle.next
            middle.next = previous
            previous = middle
            middle = temp
        
        leftList.next = previous
        current.next = end   
        return dummy.next