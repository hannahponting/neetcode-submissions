"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        first = head
        second = head
        oldToNew = {None:None}

        while first:
            oldToNew[first] = Node(first.val)
            first = first.next
        
        while second:
            node = oldToNew[second]
            node.next = oldToNew[second.next]
            node.random = oldToNew[second.random]
            second = second.next
        
        return oldToNew[head]