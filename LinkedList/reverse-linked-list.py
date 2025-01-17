206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if curr == None or curr.next == None:
            return curr
        while curr.next != None:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        curr.next = prev
        return curr
        