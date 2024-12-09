56. Merge Intervals

class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        ans = []
        for i in range(len(arr)):
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            else:
                ans[-1][1] = max(ans[-1][1], arr[i][1])
        return ans
        