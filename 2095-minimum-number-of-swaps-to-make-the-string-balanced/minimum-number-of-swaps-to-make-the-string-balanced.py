class Solution:
    def minSwaps(self, s: str) -> int:
        ct=0
        for i in range(len(s)):
            if s[i]=='[':
                ct+=1
            elif ct>0:
                ct-=1
        return (ct+1)//2
