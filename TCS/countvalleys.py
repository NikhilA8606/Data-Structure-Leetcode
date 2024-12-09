s = 'dduudduuuudd'

n = len(s)
i = 0
c,t = 0,0
while i < n:
    if s[i] == 'u':
        c += 1
        i += 1
        while c > 0 and i<n:
            if s[i] == 'd':
                c -= 1
            else:
                c += 1
            i+=1
        c = 0
    else:
        c += 1
        i += 1
        while c>0 and i<n:
            if s[i] == 'd':
                c += 1
            else:
                c -= 1
            i += 1
        t += 1

print(t)