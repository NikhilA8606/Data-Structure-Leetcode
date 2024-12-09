n1 = 3
x = [1,  5,  5] 
n2 = 5
y = [3,  4,  5,  5,  10]
n3 = 4
z = [5,  5,  10,  20]

i,j,k = 0,0,0
lis = []

while i<n1 and j<n2 and k<n3:
    if x[i] == y[j] == z[k]:
        lis.append(x[i])
        i += 1
        j += 1
        k += 1   
    elif x[i] < y[j]:
        i += 1
    elif y[j] < z[k]:
        j += 1
    else:
        k += 1
print(lis)
 
