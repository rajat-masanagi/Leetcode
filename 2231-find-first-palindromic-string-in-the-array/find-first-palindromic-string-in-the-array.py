class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            ls=-1
            ch=0
            if(len(i)%2==0):
                n=len(i)//2
            else:
                n=(len(i)-1)//2
            for j in range(n):
                if(i[j]!=i[ls]):
                    ch=1
                ls=ls-1
            if(ch==0):
                return i
        return ""

