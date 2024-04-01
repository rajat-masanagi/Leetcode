class Solution:
    def maxDepth(self, s: str) -> int:
        m=0
        sol=0
        for i in s:
            if i=='(':
                m+=1
                if m>=sol:
                    sol=m
            elif i==')':
                m-=1
        return sol
