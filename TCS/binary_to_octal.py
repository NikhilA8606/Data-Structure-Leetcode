n = "11111"

if len(n) % 3 == 1:
    s = "00" + n
elif len(n) % 3 == 2:
    s = "0" + n
else:
    s = n
he = []
for i in range(len(s)-1,-1,-3):
    he.append(int(s[i-2:i+1],2))
print("".join(str(i) for i in he[::-1]))