class MinStack:

    def __init__(self):
        self.s = []
        self.dp = [3*1e9]

    def push(self, val: int) -> None:
        self.s.append(val)
        self.dp.append(min(self.dp[-1], val))

    def pop(self) -> None:
        self.s.pop()
        self.dp.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.dp[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
