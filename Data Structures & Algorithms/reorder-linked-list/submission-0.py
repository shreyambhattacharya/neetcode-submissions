# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        nodes = []
        size = 0

        currNode = head
        while currNode:
            nodes.append(currNode)
            currNode = currNode.next
            size += 1
        
        currNode = head
        for i in range(size//2):
            poppedNode = nodes.pop()
            nextNode = currNode.next
            currNode.next = poppedNode
            poppedNode.next = nextNode
            currNode = nextNode
        
        currNode.next = None