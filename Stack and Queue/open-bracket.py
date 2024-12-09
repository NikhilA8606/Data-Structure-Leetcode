lis = []
a = "-(a-b-c)"
b = "-a+b+c"
n = len(a)
i = 0

while (i<n):
    if a[i] == '(':   
        temp = lis[-1]
        i += 1
        while a[i] != ')':
            if a[i].isalpha() or temp == '+':
                lis.append(a[i])
            elif temp == '-' and a[i]=='+':
                lis.append('-')
            elif temp == '-' and a[i] == '-':
                lis.append('+')
            i += 1      
    else:
        lis.append(a[i])
    i += 1

for i in range(len(b)-1,-1,-1):
    if lis[-1] != b[i]:
        print("False")
    else:
        lis.pop()
print("True")
