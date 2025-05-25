class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d={}
        for i in words:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        flag=0
        ans=0
        for i in d:
            if i[0]==i[1]:
                if d[i]%2!=0:
                    flag=1
                if d[i]>=2:
                    z=min(d[i],d[i[::-1]])
                    z=z-z%2
                    ans+=z

            elif i[::-1] in d.keys():
                z=min(d[i],d[i[::-1]])
                ans+=z
        return ans*2+flag*2
        
