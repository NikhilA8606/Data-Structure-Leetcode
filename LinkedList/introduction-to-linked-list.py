https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-linked-list

Construct the linked list from arr and return the head of the linked list.
Example 1:
Input:
n = 5
arr = [1,2,3,4,5]
Output:
1 2 3 4 5
Explanation: Linked list for the given array will be 1->2->3->4->5.

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        if not arr:
            return None
            
        head = Node(arr[0])
        curr = head
        
        for i in arr[1:]:
            curr.next = Node(i)
            curr = curr.next
        return head