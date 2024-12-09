189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k = k % n
        if k == 0:
            return

        k = n - k  # Adjust k to length - k

        # Rotate the array in place
        nums[:] = nums[k:] + nums[:k]

# left rotation
# array = [3,7,8,9,10,11]
# n = len(array)
# k = 3
# k = k%n
# k = n-k
# array[:] = array[n-k:] + array[:n-k]
# print(array)


        