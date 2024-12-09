a = [7,9,4,3,2]
k = 3
ind = [0,3]

k = k % len(a)

c = len(a) - k

lis = a[c:] + a[:c]
res =[]

for i in ind:
    res.append(lis[i])
print(res)