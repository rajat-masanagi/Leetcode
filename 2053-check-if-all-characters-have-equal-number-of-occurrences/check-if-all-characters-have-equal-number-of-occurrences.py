class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i not in list(d.keys()):
                d.update({i:1})
            else:
                d[i]+=1
        if len(set(list(d.values())))==1:
            return True
        else:
            return False