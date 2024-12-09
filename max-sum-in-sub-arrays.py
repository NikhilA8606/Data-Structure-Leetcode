https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays

Maximum Score from Subarray Minimums


class Solution:
    def pairWithMaxSum(self, arr):
        res=arr[0]+arr[1]
        
        i=1
        j=2
        while i<len(arr)-1 and j<len(arr):
            s=arr[i]+arr[j]
            
            res=max(s,res)
            i+=1
            j+=1
        return res