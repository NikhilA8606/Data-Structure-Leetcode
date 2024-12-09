735. Asteroid Collision

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s = []
        for i in a:
            while s and i < 0 < s[-1]:
                if s[-1] < abs(i):
                    s.pop()
                    continue
                elif s[-1] == abs(i):
                    s.pop()
                break
            else:
                s.append(i)
        
        return s