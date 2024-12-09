https://takeuforward.org/data-structure/replace-elements-by-its-rank-in-the-array/

nums = [20, 15, 26, 2, 98, 6]
lis = sorted(nums)
dic =  {}
s = 1
for i in lis:
    if i not in dic:
        dic[i] = s
        s += 1
res = [dic[i] for i in nums] 
print(res)

