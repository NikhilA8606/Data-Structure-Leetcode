a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(a)

for i in range(n):
    s = i + 1
    e = a[i] + i 
    for j in range(s,e+1):
        ans = a[i] + 