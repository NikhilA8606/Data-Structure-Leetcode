8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespace
        s = s.lstrip()
        if not s:  # Return 0 if the string is empty after stripping
            return 0

        # Step 2: Determine the sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Step 3: Convert digits to an integer
        ans = 0
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + (ord(s[i]) - ord('0'))
            i += 1

        # Apply the sign
        ans *= sign

        # Step 4: Clamp the result within the 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX

        return ans
