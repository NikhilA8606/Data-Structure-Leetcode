https://www.interviewbit.com/problems/min-stack/

class MinStack:
    
    def __init__(self):
        self.arr = []
        self.mini = []
    # @param x, an integer
    def push(self, x):
        self.arr.append(x)
        if  not self.mini or x<=self.mini[-1]:
            self.mini.append(x)

    # @return nothing
    def pop(self):
        if self.arr:
            y = self.arr.pop()
            if y == self.mini[-1]:
                self.mini.pop()
        
    # @return an integer
    def top(self):
        if self.arr:
            return self.arr[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if self.mini:
            return self.mini[-1]
        else:
            return -1
            

