arr = [1,2,3,4,5]
n = len(arr)
def revers(i):
    if i>=n/2:
        return
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n - i - 1] = temp
    revers(i+1)
revers(0)
print(arr)
