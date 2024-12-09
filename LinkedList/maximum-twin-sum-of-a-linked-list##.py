2130. Maximum Twin Sum of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        # Step 2: Calculate maximum twin sum
        n = len(values)
        max_twin_sum = float('-inf')
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_twin_sum = max(max_twin_sum, twin_sum)
        
        return max_twin_sum


# curr = head
#         c = 1
#         while curr.next:
#             curr = curr.next
#             c += 1
#         i = 0
#         curr = head
#         tail = head
#         twin = float('-inf')
#         while i < c/2:
#             k = c - i - 1
#             for i in range(k):
#                 tail = tail.next
#             sum = curr.val + tail.val
#             twin = max(twin,sum)
#             curr = curr.next
#             tail = curr
#             i += 1
#         return twin
        