import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h=nums
        heapq.heapify(self.h)
        self.k=k
        while len(self.h)>k:
            heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h)<self.k:
            heappush(self.h,val)
        elif val>self.h[0]:
            heapreplace(self.h,val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)