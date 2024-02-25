class Solution:
    def reverseVowels(self, s: str) -> str:
        vi=[]
        r=list(s)
        for i in range(len(s)):
            if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or
               s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
                vi.append(i)
        for i in range(len(vi)//2):
            r[vi[i]],r[vi[-1-i]]=r[vi[-1-i]],r[vi[i]]
        res=""
        for i in r:
            res=res+i
        return res