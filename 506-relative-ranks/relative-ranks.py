import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=['']*len(score)
        h=[]
        for i in range(len(score)):
            heappush(h,(-score[i],i))
        k=0
        for i in range(len(score)):
            z=heappop(h)
            if i==0:
                ans[z[1]]='Gold Medal'
            elif i==1:
                ans[z[1]]='Silver Medal'
            elif i==2:
                ans[z[1]]='Bronze Medal'
            else:
                k+=1
                ans[z[1]]=str(k+3)
        return ans