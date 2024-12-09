20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        i = 0
        while i<len(s):
            if s[i] == '(' or s[i] =='{' or s[i] =='[':
                lis.append(s[i])
            else:
                if not lis:
                    return False
                if s[i] == ')':
                    if lis[-1] != '(':
                        return False
                    lis.pop()
                elif s[i] == '}':
                    if lis[-1] != '{':
                        return False
                    lis.pop()
                elif s[i] == ']':
                    if lis[-1] != '[':
                        return False
                    lis.pop()
                else:
                    return False
            i += 1
        if lis:
            return False
        else:
            return True
        
            
                
                

        
        
        