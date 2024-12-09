232. Implement Queue using Stacks (Amortized method)

class MyQueue:

    def __init__(self):
       self.ip = []
       self.op = []

    def push(self, x: int) -> None:
        self.ip.append(x)

    def pop(self) -> int:
        if len(self.op)!=0:
            return self.op.pop()
        else:
            while len(self.ip)>0:
                self.op.append(self.ip.pop())
            return self.op.pop()

    def peek(self) -> int:
        if len(self.op)!=0:
            return self.op[-1]
        else:
            while len(self.ip)>0:
                self.op.append(self.ip.pop())
            return self.op[-1]

    def empty(self) -> bool:
        return len(self.op) == 0 and len(self.ip) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()