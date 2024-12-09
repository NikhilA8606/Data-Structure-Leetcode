# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=given-a-linked-list-of-0s-1s-and-2s-sort-it

# Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

# Example 1:

# Input:
# N = 8
# value[] = {1,2,2,1,2,0,2,2}
# Output: 0 1 1 2 2 2 2 2
# Explanation: All the 0s are segregated
# to the left end of the linked list,
# 2s to the right end of the list, and
# 1s in between.

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        d_zero = Node(0)
        d_one = Node(0)
        d_two = Node(0)
        
        z_head = d_zero
        o_head = d_one
        t_head = d_two
        
        while head:
            if head.data == 0:
                z_head.next = Node(0)
                z_head = z_head.next
                
            elif head.data == 1:
                o_head.next = Node(1)
                o_head = o_head.next
                
            elif head.data == 2:
                t_head.next = Node(2)
                t_head = t_head.next
            
            head = head.next
            
        if d_one.next:
            z_head.next = d_one.next
            o_head.next = d_two.next
        else:
            z_head.next = d_two.next
        
        return d_zero.next