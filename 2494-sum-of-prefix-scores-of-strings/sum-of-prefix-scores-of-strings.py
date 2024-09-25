class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        h={}
        for i in words:
            t=''
            for j in i:
                t=t+j
                if t in h.keys():
                    h[t]+=1
                else:
                    h.update({t:1})
        ans=[]
        for i in words:
            t=''
            c=0
            for j in i:
                t=t+j
                c+=h[t]
            ans.append(c)
        return ans