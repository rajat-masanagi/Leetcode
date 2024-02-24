class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=address.split(".")
        t=""
        for i in s:
            t=t+i+"[.]"
        return t[:-3]