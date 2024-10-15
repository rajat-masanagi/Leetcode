import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        h=[]
        ans=[]
        for i in range(len(mat)):
            z=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    z+=1
                else:
                    break
            heappush(h,(z,i))
        while k>0:
            val=heappop(h)
            ans.append(val[1])
            k-=1
        return ans