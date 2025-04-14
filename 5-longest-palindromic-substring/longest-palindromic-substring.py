class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(pal):
            if pal==pal[::-1]:
                return True
            else:
                return False
        ans=""
        maxlen=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                p=s[i:j+1]
                if palindrome(p):
                    if len(p)>maxlen:
                        maxlen=len(p)
                        ans=p
        return ans