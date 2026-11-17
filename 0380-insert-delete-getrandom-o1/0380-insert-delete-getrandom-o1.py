class RandomizedSet:

    def __init__(self):
        self.lst=[]
        self.mp={}
        

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.mp[val]=len(self.lst)
        self.lst.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False

        idx=self.mp[val]
        last=self.lst[-1]
        self.lst[idx]=last
        self.mp[last]=idx
        self.lst.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()