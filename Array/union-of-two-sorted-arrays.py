https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arraysclass Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        i = 0
        j = 0
        lis = []
        while i<n and j<m:
            if arr1[i] <= arr2[j]:
                if not lis or arr1[i] != lis[-1]:
                    lis.append(arr1[i])
                i += 1
            else:
                if not lis or arr2[j] != lis[-1]:
                    lis.append(arr2[j])
                j += 1
        while j < m:
            if not lis or arr2[j] != lis[-1]:
                    lis.append(arr2[j])
            j += 1
        while i < n:
            if not lis or arr1[i] != lis[-1]:
                    lis.append(arr1[i])
            i += 1
        return lis