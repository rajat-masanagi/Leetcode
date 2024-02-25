class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s.split(" "))
        for i in range(len(l)):
            if(i==0):
                res=l[i][::-1]
            else:
                res=res+" "+l[i][::-1]
        return res
        
