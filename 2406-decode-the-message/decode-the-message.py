class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        k=key.replace(" ","")
        s=""
        for i in k:
            if(len(s)!=26):
                if i not in set(s):
                    s=s+i
            else:
                break
        res=""
        for i in message:
            if(i!=" "):
                res=res+chr(s.find(i)+97)
            else:
                res=res+" "
        return res