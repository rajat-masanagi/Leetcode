class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        t=''
        pt=0
        spc_pt=spaces[pt]
        for i in range(len(s)):
            if i==spc_pt:
                t=t+" "+s[i]
                pt+=1
                if pt<len(spaces):
                    spc_pt=spaces[pt]
            else:
                t=t+s[i]
        return t
