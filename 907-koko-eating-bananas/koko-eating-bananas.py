import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            total_hours=0
            for i in piles:
                total_hours+= (i+mid-1)//mid
            if total_hours>h:
                left=mid+1
            else:
                right=mid-1
        return left
