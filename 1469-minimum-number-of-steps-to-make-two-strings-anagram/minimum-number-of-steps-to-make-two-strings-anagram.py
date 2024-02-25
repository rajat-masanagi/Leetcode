class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1={}
        for i in s:
            if i not in set(d1.keys()):
                d1.update({i:1})
            else:
                d1[i]+=1
        for i in t:
            if i not in set(d1.keys()):
                d1.update({i:-1})
            else:
                d1[i]-=1
        res=0
        print(d1)
        for i in list(d1.values()):
            if i<0:
                res+=i*-1
        return res

                