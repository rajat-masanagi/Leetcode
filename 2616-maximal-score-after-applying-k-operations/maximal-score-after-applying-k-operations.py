import heapq
math.ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        n=len(nums)
        h=[]
        for i in range(n):
            heappush(h,-nums[i])
        score=0
        for i in range(k):
            v=-heappop(h)
            score+=v
            heappush(h,-math.ceil(v/3))
        return score
