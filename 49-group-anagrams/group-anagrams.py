class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        at=[]
        for i in range(len(strs)):
            at.append([''.join(sorted(strs[i])),i])
        bt=sorted(at)
        ans=[]
        si=set()
        o=[]
        for i in range(len(strs)):
            if bt[i][0] in si:
                o.append(strs[bt[i][1]])
            else:
                si.add(bt[i][0])
                ans.append(o)
                o=[strs[bt[i][1]]]
        ans.append(o)
        ex=ans.pop(0)
        return ans

            

        

