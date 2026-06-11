# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]

        while len(lists) >1:
            list1 = lists.pop()
            list2 = lists.pop()

            dummy = node = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next

            while list1:
                node.next = list1
                list1 = list1.next
                node = node.next

            while list2:
                node.next = list2
                list2 = list2.next
                node = node.next
            lists.append(dummy.next)
        return lists[0]
            

