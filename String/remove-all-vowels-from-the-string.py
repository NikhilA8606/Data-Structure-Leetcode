# Example 1:
# Input: Str = “take u forward”
# Output: tk  frwrd
# Explanation: All vowels are removed from the given String.

# Example 2:
# Input: Str = “I am very happy today”
# Output:  m vry happy tdy
# Explanation: All vowels are removed from the given String.

Str = "I am very happy today"
v = ['a','e','i','o','u']
temp = list(Str)

for i in Str:
    if i in v:
        temp.remove(i)
        
print(''.join(temp))
