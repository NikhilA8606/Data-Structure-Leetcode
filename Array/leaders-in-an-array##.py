Array Leaders

https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        lis = []
        for i in range(n-1,-1,-1):
            if not lis or arr[i] >= lis[-1]:
                lis.append(arr[i])
     
        return lis[::-1]