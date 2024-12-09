# https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=add-1-to-a-number-represented-as-linked-list

# A number n is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it. Returns the head of the modified linked list. The driver code prints the number.

# Note: The head represents the left-most digit of the number.

# Examples :

# Input: LinkedList: 4->5->6
# Output: 457
# Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def addOne(self, head):
        def helper(node):
            if not node:
                return 1
            
            carry = helper(node.next)
            total = node.data + carry
            
            node.data = total % 10
            return total // 10
        
        carry = helper(head)
        
        if carry:
            new_head = ListNode(carry)
            new_head.next = head
            head = new_head
        
        return head