import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h=[]
        for i in nums:
            h.append(-i)
        heapify(h)
        v1=-heappop(h)-1
        v2=-heappop(h)-1
        return v1*v2
