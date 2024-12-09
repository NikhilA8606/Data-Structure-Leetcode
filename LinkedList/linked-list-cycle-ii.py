142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        f = head
        s = head
        n = head
        c = 0
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                while n != f:
                    n = n.next
                    f = f.next        
                return n
        return None
            
        