# https://www.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-length-of-loop

# Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks 
# whether a given Linked List contains a loop or not and if the loop is present then return the count 
# of nodes in a loop or else return 0. C is the position of the node to which the last node is connected.
# If it is 0 then no loop.

def countNodesinLoop(head):
    if not head or not head.next:
        return 0
    f = head
    s = head
    while f and f.next:
        f = f.next.next
        s = s.next
        if f == s:
            c = 1
            f = f.next
            while f != s:
                c += 1
                f = f.next
            return c
    return 0