a = [1, 3, -1, 4, -3, -5, -6, 3, 7]

l = 0
r = 1

n = len(a)

while r<n:
    if a[l] > 0:
        l += 1
        r += 1
    elif a[r] < 0:
        r += 1
    else:
        t = a[l]
        a[l] = a[r]
        a[r] = t
print(a)