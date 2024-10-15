import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=stones
        for i in range(len(stones)):
            h[i]=-h[i]
        heapify(h)
        while len(h)>1:
            x=heappop(h)
            y=heappop(h)
            if x==y:
                continue
            else:
                heappush(h,-abs(x-y))
        if len(h)!=1:
            return 0
        return -h[0]