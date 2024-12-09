92. Reverse Linked List ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if not head or not head.next or l==r:
            return head
        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        curr = head

        for i in range(l-1):
            left = left.next
            curr = curr.next
        
        sub = curr
        prev = None
        for i in range(r-l+1):
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        left.next = prev
        sub.next = curr

        return dummy.next
        
        
        