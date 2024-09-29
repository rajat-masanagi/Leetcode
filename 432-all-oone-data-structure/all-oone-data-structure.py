class AllOne:

    def __init__(self):
        self.ma=''
        self.max=0
        self.d={}

    def inc(self, key: str) -> None:
        if key in self.d.keys():
            self.d[key]+=1

            if self.d[key]>self.max:
                self.max=self.d[key]
                self.ma=key
                
        else:
            self.d[key]=1
            if self.ma=="":
                self.ma=key
                self.max=1

    def dec(self, key: str) -> None:
        self.d[key]-=1

        if self.d[key]==0:
            del self.d[key]

            if key==self.ma:
                self.ma=""
                self.max=0

        else:
            if key==self.ma:
                self.ma=max(zip(self.d.values(), self.d.keys()))[1]
                self.max=self.d[self.ma]

    def getMaxKey(self) -> str:
        return self.ma

    def getMinKey(self) -> str:
        if not self.d:
            return ""
        else:
            return min(zip(self.d.values(), self.d.keys()))[1]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()