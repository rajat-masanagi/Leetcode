class Solution:
    def sortSentence(self, s: str) -> str:
        ss=list(s.split(" "))
        L=[""]*len(ss)
        for i in ss:
            L[int(i[-1])-1]=i[:-1]
        for i in range(len(L)):
            if i==0:
                res=L[i]
            else:
                res=res+" "+L[i]
        return res
