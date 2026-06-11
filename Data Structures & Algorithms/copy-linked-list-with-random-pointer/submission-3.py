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
        oldToCopy = {None: None}

        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            node = oldToCopy[curr]
            node.next = oldToCopy[curr.next]
            node.random = oldToCopy[curr.random]
            node = node.next
            curr = curr.next
    
        return oldToCopy[head]
        
        