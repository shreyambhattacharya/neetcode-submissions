# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        ptr = head
        while ptr:
            size += 1
            ptr = ptr.next
        
        if n == size:
            return head.next

        ptr = head
        for i in range(size-n-1):
            ptr = ptr.next
        ptr.next = ptr.next.next
        
        return head