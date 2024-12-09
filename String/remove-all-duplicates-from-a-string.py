# Problem Statement: Given a String remove all the duplicate characters from the given String.
# Examples:

# Example 1:
# Input: s = "bcabc"
# Output: “bca"

# Explanation: Duplicate Characters are removed
# Example 2:
# Input: s = "cbacdcbc"
# Output: "cbad" 
# Explanation: Duplicate Characters are removed
from collections import Counter
s = "bcabc"
dic = Counter(s)
res = []
for i in dic:
    res.append(i)
print(''.join((res)))
