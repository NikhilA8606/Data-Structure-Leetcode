48. Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1
        temp = list()

        while l < r:
            temp = matrix[r]
            matrix[r] = matrix[l]
            matrix[l] = temp
            l += 1
            r -= 1
            print(temp)
        k = 0
        for i in zip(*matrix):
            matrix[k] = list(i)
            k += 1
        
        