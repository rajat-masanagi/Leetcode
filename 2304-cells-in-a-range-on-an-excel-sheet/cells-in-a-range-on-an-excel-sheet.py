class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        L=[]
        a=list(s.split(":"))
        l2=ord(a[1][0])
        l1=ord(a[0][0])
        n2=int(a[1][1:])
        n1=int(a[0][1:])
        for i in range(l2-l1+1):
            for j in range(n2-n1+1):
                L.append(chr(l1+i)+str(n1+j))
        return L


