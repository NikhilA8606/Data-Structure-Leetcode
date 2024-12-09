n = 5
m = [1,1,2,5,2]

m[0] = 3
m[3] = 2

l = 0
r = 1

while r < n:
    if m[l] != m[r]:
        l += 1
        m[l] = m[r]
    r += 1

print(len(m[:l+1]))