class Solution:
    def minimumSteps(self, s: str) -> int:
        p1=0
        ans=0
        for i in range(len(s)):
            if s[i]=='1':
                p1+=1
            elif s[i]=='0':
                ans+=p1
        return ans
