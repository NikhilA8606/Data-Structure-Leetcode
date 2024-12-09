19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        f = head
        s = head
        for i in range(n):
            f = f.next
        if f.next == None:
            return s.next.next
        while f.next != None:
            f = f.next
            s = s.next
        s.next = s.next.next
        return dummy.next
        
            
            



            
