# Problem Statement: Write a program to find a word in a given string that has the highest number of repeated letters. If not found, return -1.

# Examples:

# Example 1:
# Input: string=”abcdefghij google microsoft”
# Output: google
# Explanation: In “google” g appears 2 times, o appears 2 times which is highest among all words

# Example 2:
# Input: string = “cameron blue”
# Output: -1
# Explanation: No word has more than 1 letter.

from collections import Counter
s = "abcdefghij google microsoft".split()
maxv = -1
for word in s:
    dic = Counter(word)
    m = max(dic.values())
    if m>maxv:
        res = word
        maxv = m
if m == 1:
    print(-1)
else:
    print(res)