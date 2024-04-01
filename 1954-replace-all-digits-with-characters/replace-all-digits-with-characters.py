class Solution:
    def replaceDigits(self, s: str) -> str:
        t=''
        for i in range(len(s)):
            if(i%2==0):
                t=t+s[i]
            else:
                t=t+chr(ord(s[i-1])+int(s[i]))
        return t