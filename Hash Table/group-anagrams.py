# 49. Group Anagrams

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = defaultdict(list)
        res = []
        for s in strs:
            sort = tuple(sorted(s))
            ang[sort].append(s)
        for val in ang.values():
            res.append(val)
        return res        
        