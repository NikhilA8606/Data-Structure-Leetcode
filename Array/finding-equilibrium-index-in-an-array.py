https://takeuforward.org/data-structure/finding-equilibrium-index-in-an-array/

nums = [1,-1,4]
eq,l,r = 0,0,sum(nums)
for i in range(len(nums)):
    r -= nums[i]
    if l==r:
        eq = i
        break
    l += nums[i]
print(i)