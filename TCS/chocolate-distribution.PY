class Solution:
    
    def findMinDiff(self, A, N, M):
        # Sort the array to easily access subarrays with minimal difference
        A.sort()
        
        # Initialize minimum difference to a large value
        mini = float('inf')
        
        # Use a sliding window of size M
        for i in range(N - M + 1):
            diff = A[i + M - 1] - A[i]
            if diff < mini:
                mini = diff
        
        return mini