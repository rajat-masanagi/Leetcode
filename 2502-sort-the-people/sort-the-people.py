class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d=list(zip(names,heights))
        j=sorted(d,key=lambda x:x[1],reverse=True)
        k=[]
        for n,h in j:
            k.append(n)
        return k

