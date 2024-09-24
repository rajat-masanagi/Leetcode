class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        for i in range(x):
            ans=i
            if i*i>=x:
                break
        if x==1:
            return 1
        if x==2:
            return 1
        if x==ans*ans:
            return ans
        else:
            return ans-1
