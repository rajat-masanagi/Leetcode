class Solution:
    def countAsterisks(self, s: str) -> int:
        e=0
        res=0
        for i in s:
            if i=='|':
                e=e+1
            if e%2==0:
                if i=="*":
                    res=res+1
        return res
            