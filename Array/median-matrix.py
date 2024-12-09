# find the minimum of median of each row of matrix
n = 5
# m  = [[34,77,72,65],[49,70,71,15],[12,84,5,78],[74,1,26,60]]
# m= [[1,5,2,3],[4,5,2,1],[1,1,2,3],[1,5,2,4]]
m = [[1,5,2,4,5],[1,6,9,7,12],[4,5,6,7,12],[1,5,2,1,4],[5,1,5,4,5]]

def median(arr):
    arr.sort()
    if n % 2 != 0:
        return arr[n//2]
    else:
        f = arr[n//2 - 1]
        b = arr[n//2]
        return (f+b)/2
        
mini = float("inf")
for i in m:
    med = median(i)
    mini = min(med,mini)
print(mini)



