# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=search-in-linked-list-1664434326

# Given a linked list of n nodes and a key , the task is to check if the key is present in the linked list or not.

class Solution:
    def searchKey(self, n, head, key):
        while head:
            if head.data == key:
                return True
            head = head.next
        return False