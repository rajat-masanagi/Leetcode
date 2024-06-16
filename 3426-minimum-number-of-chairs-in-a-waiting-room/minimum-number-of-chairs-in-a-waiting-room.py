class Solution:
    def minimumChairs(self, s: str) -> int:
        r=0
        c=0
        for i in s:
            if i=='E':
                c=c+1
            else:
                c=c-1
            if(c>r):
                r=c
        return r