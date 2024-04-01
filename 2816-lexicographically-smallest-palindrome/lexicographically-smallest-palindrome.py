class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n=len(s)//2
        j=len(s)-1
        t=""
        for i in range(n):
            if(s[i]!=s[j]):
                if(s[i]<s[j]):
                    t=t+s[i]
                else:
                    t=t+s[j]
            else:
                t=t+s[i]
            j-=1
        if(len(s)%2!=0):
            t=t+s[n]+t[::-1]
        else:
            t=t+t[::-1]
        return t
        