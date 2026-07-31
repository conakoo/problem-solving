class Logger:

    def __init__(self):
        self.dic = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.dic[message] <= timestamp:
            if self.dic[message] == 0:
                self.dic[message] = timestamp+10
            else:
                self.dic[message] += 10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
