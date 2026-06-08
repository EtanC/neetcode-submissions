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
        if not head:
            return None
            
        storage: dict['Node', 'Node'] = {}
        curr: Optional['Node'] = head

        # first pass: create all new nodes
        while curr is not None:
            storage[curr] = Node(curr.val)
            curr = curr.next
        
        # second pass: wire up pointers
        curr = head
        while curr is not None:
            storage[curr].next = storage[curr.next] if curr.next else None
            storage[curr].random = storage[curr.random] if curr.random else None
            curr = curr.next

        return storage[head]