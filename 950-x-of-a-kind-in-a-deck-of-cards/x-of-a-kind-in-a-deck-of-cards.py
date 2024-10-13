class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d={}
        for i in deck:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        s=set(d.values())
        mi=min(s)
        if mi==1:
            return False
        factors=set()
        for i in range(2,mi+1):
            if mi%i==0:
                factors.add(i)
        for i in factors:
            ct=0
            for j in s:
                if j%i==0:
                    ct+=1
            if ct==len(s):
                return True
        return False
