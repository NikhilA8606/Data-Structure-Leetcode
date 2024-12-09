# Example 1:
# Input: String str = "take u forward is awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: We get the result after capitalizing the first and last character of each word of a string

# Example 2:
# Input: String str = "Take u Forward is Awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: Characters T, F, A are initially in uppercase , so they remain as they are in the result

Str ="take u forward is awesome"
words = Str.split()
res = []
for word in words:
    if len(word) == 1:
        res.append(word.upper())
    else:
        add = word[0].upper() + word[1:-1] + word[-1].upper()
        res.append(add)
print(' '.join(res))