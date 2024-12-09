https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bit-manipulation

class Solution:
    def bitManipulation(self, num, i):
        i -= 1
        g = (num >> i) & 1
        s = num | (1<<i)
        c = num & (~(1<<i))
        print(g,s,c)