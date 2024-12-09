Implement Queue using array

# https://www.geeksforgeeks.org/problems/implement-queue-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-queue-using-array

class MyQueue:
    
    def __init__(self):
        self.arr = []
        
    #Function to push an element x in a queue.
    def push(self, x):
         self.arr.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.arr:
            return -1
        else:
            return self.arr.pop(0)