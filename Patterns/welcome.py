s = "welcome"
n = len(s)
t1 = 0
t2 = n-1
for i in range(n):
    for j in range(n):
        if j == t1:
            print(s[t1],end="")
        elif j == t2:
            print(s[t2],end="")
        else:
            print(" ",end="")
    t1 += 1
    t2 -= 1
    print()

# w     e
#  e   m 
#   l o  
#    c   
#   l o  
#  e   m 
# w     e
