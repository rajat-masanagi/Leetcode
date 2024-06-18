class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm=[]
        pt1=0
        pt2=len(s)
        for i in s:
            if(i=='I'):
                perm.append(pt1)
                pt1+=1
            else:
                perm.append(pt2)
                pt2-=1
        if s[-1]=="I":
            perm.append(perm[-1]+1)
        else:
            perm.append(perm[-1]-1)
        return perm