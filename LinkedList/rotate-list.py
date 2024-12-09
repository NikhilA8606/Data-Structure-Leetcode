61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        c = 1
        while curr.next:
            curr = curr.next
            c += 1
        
        k = k % c #Total no of rotations
        if k == 0:
            return head
        k = c - k
        curr.next = head # here tail is linked to head but curr is still at tail
        while k > 0:
            curr = curr.next
            k -= 1
        
        head = curr.next
        curr.next = None
        return head
        


            


        