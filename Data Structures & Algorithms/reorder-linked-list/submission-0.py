# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        storage: List[ListNode] = []
        curr: ListNode = head

        while curr:
            storage.append(curr)
            curr = curr.next

        left: int = 0
        right: int = len(storage) - 1

        while left < right: 
            storage[left].next = storage[right]
            left += 1
            if left == right: 
                break 
            storage[right].next = storage[left]
            right -= 1
        
        storage[left].next = None
    