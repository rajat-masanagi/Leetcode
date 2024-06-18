class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        d1=0
        d2=0
        for i in range(len(s)):
            if(i<len(s)//2):
                if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                    d1+=1
            else:
                if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                    d2+=1
        if d1==d2:
            return True
        else:
            return False