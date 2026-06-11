# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            list1 = lists.pop()
            list2 = lists.pop()
            res = dummy = ListNode(0)

            while list1 and list2:
                if list1.val < list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                dummy = dummy.next

            while list1:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            while list2:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
            lists.append(res.next)
        return lists[0]
                

