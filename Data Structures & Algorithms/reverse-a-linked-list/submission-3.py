# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, node = None, head

        while node:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
        return previous