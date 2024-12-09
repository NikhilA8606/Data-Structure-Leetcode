2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 != None or l2 != None:
            sum = c
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val
            
            n = ListNode(sum%10)
            c = int(sum/10)
            curr.next = n
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if c:
            n = ListNode(c)
            curr.next = n
        return dummy.next

        
        