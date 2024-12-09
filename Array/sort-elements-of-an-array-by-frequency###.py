https://takeuforward.org/data-structure/sort-elements-of-an-array-by-frequency/

array = [1,2,3,2,4,3,1,2]
dic = {}
for i in set(array):
    dic[i] = array.count(i)
new = dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
lis = []
for i in new:
    lis.extend([i]*new[i])
print(lis)
    
