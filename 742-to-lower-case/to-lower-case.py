class Solution:
    def toLowerCase(self, s: str) -> str:
        res=""
        for i in s:
            if(ord(i)>=65 and ord(i)<=90):
                res=res+chr(96+ord(i)-64)
            else:
                res=res+i
        return res