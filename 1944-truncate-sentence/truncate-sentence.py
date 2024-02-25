class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        r=s.split(" ")
        f=r[:k]
        for i in range(k):
            if(i==0):
                res=f[i]
            else:
                res=res+" "+f[i]
        return res