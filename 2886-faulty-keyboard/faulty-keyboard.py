class Solution:
    def finalString(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            if s[i]=='i':
                res=res[:i][::-1]
            else:
                res=res+s[i]
        return res