class Solution:
    def freqAlphabets(self, s: str) -> str:
        s=s[::-1]
        t=''
        i=0
        while(i<len(s)):
            if(s[i]=='#'):
                t=t+chr(96+int(s[i+2]+s[i+1]))
                i=i+2
            else:
                t=t+chr(96+int(s[i]))
            i=i+1
        return t[::-1]