148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
                return head
        def mid(node):
            f = node
            s = node
            prev = None
            while f and f.next:
                f = f.next.next
                prev = s
                s = s.next
            return prev

        def merge(l1,l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                curr = curr.next
            while l1:
                curr.next = ListNode(l1.val)
                l1 = l1.next
                curr = curr.next
            while l2:
                curr.next = ListNode(l2.val)
                l2 = l2.next
                curr = curr.next
            return dummy.next
        m = mid(head)
        l = head
        r = m.next
        m.next = None

        l = self.sortList(l)
        r = self.sortList(r)

        return merge(l,r)

        

        
        