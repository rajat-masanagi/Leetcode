class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        z=0
        for i in s:
            if i=="L":
                z=z+1
            else:
                z=z-1
            if z==0:
                count=count+1
        return count