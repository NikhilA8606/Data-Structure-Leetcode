Reverse a Doubly Linked List

https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=reverse-a-doubly-linked-list



'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        curr = head
        while curr:
           nxt = curr.next
           curr.next = curr.prev
           curr.prev = nxt
           r = curr
           curr = nxt
        return r