class Solution:
    def decodeString(self, s: str) -> str:
        sk = []
        nk = []
        i = 0
        while i < len(s):
            if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isdigit():
                ex = s[i] + s[i+1] + s[i+2]
                nk.append(int(ex))
                i += 3
            elif s[i].isdigit() and s[i+1].isdigit():
                ex = s[i] + s[i+1]
                nk.append(int(ex))
                i += 2
            elif s[i].isdigit():
                nk.append(int(s[i]))
                i += 1
            else:
                if s[i] == ']':
                    t = []
                    while sk[-1] != '[':
                        t.append(sk.pop())
                    sk.pop()
                    n = nk.pop()
                    x = ''.join(t[::-1]) * n
                    sk.append(x)
                    i += 1
                else:
                    sk.append(s[i])
                    i += 1
        return ''.join(sk)
