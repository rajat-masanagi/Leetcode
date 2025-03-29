class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        quo=maxWeight//w
        maxq=n*n
        return min(quo,maxq)