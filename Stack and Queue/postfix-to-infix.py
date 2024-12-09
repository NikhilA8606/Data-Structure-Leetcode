lis = []
s = "abd*+ef/g*-"
i = 0
while i<len(s):
    if s[i].isalpha():
        lis.append(s[i])
    else:
        x = lis.pop()
        y = lis.pop()
        lis.append(y + s[i] + x)
    i += 1
print(lis)