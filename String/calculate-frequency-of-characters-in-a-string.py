# Example 1:
# Input: takeuforward
# Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 
# Explanation: Count of every character of string is printed.

# Example 2:
# Input: articles
# Output: a1 c1 e1 i1 l1 r1 s1 t1 
# Explanation: Count of every character of string is printed

word = "articles"
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
new = dict(sorted(dic.items(),key=lambda x:x[0]))
lis = []
for i in new:
    lis.append(i + str(dic[i]))
print(" ".join(lis))

    
