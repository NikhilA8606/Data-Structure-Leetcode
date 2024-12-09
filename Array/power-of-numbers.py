https://www.naukri.com/code360/problems/power-of-numbers_8157729?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from typing import *

def power(x: int, n: int) -> int:
    ans = 1
    MOD = 10**9 + 7
    while n > 0:
        if n % 2 == 1:
            ans *= x
            n -= 1
        else:
            n //= 2  # Use integer division
            x *= x
    return ans % MOD