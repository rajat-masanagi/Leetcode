import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((-1+math.sqrt(1+8*n))/2)