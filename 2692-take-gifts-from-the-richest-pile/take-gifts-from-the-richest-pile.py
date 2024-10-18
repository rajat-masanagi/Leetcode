import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ans=0
        arr=[]
        for i in gifts:
            arr.append(-i)
        h=arr
        heapify(arr)

        for i in range(k):
            val=int(math.floor(math.sqrt(-heappop(h))))
            heappush(h,-val)

        for i in h:
            ans+=-i
        return ans
            
