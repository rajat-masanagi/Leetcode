class Solution:
    def countKeyChanges(self, s: str) -> int:
        flag=0
        k=s.lower()
        for i in range(len(k)-1):
            if k[i]!=k[i+1]:
                flag+=1
        return flag