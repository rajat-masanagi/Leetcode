class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        se=set(s1)
        d={}
        for i in s1:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        m=len(s2)
        n=len(s1)
        for i in range(m-n+1):
            temp={}
            for j in range(i,i+n):
                if s2[j] in temp.keys():
                    temp[s2[j]]+=1
                else:
                    temp[s2[j]]=1
            if temp==d:
                return True
        return False
                