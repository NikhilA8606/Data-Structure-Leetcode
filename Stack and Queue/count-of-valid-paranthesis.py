p = ")()()"
s = []
c = 0
for i in p:
    if s and s[-1] == "(" and i == ")":
        c += 2
        s.pop()
    else:
        s.append(i)
print(c)
