# https://www.naukri.com/code360/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=PROBLEM
# Frog Jump


def frogJump(n: int, h: List[int]) -> int:

   dp = [0 for i in range(n)]
   r = float("inf")
   for i in range(1,n):
       l = dp[i-1] + abs(h[i] - h[i-1])
       if i > 1:
           r = dp[i-2] + abs(h[i] - h[i-2])
       dp[i] = min(l,r)
   return dp[n-1]