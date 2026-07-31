class RandomizedSet:

    def __init__(self):
        self.dic = {} # val -> index of val in arr
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        i = self.dic[val]
        last = self.arr[-1]
        self.arr[i] = last # move last element to i
        self.dic[last] = i # update dic for last element
        self.arr.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
