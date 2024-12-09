d = [0 for i in range(6)]
d[0] = 1
for i in range(1,6):
    d[i] = d[i-1] * i
print(d[5])