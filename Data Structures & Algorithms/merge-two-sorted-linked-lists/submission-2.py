# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        response = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                response.next = list1
                list1 = list1.next
            else:
                response.next = list2
                list2 = list2.next
            response = response.next

        response.next = list1 or list2
        return dummy.next