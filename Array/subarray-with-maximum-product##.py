# https://www.naukri.com/code360/problems/subarray-with-maximum-product_6890008?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=SUBMISSION
# Subarray with Maximum Product

from typing import *

def subarrayWithMaxProduct(arr : List[int]) -> int:
    pre,suf = 1,1
    n = len(arr)
    res = float("-inf")
    for i in range(n):
        if pre == 0:
            pre = 1
        if suf == 0:
            suf = 1
        pre = pre * arr[i]
        suf = suf * arr[n-i-1]
        res = max(res,max(pre,suf))
    return res