class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a1=max(nums)
        temp=nums.copy()
        temp.remove(a1)
        a2=max(temp)
        temp.remove(a2)
        a3=max(temp)
        b2=min(nums)
        nums.remove(b2)
        b3=min(nums)
        if a1*a2*a3>a1*b2*b3:
            return a1*a2*a3
        else:
            return a1*b2*b3