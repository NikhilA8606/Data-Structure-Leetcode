1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        if len(set(dic.values())) != len(set(arr)):
            return False
        else:
            return True
        
            
        