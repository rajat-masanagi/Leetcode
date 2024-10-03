class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem=sum(nums)%p
        prefixsum=0
        prefixmod={0:-1}
        n=len(nums)

        if rem==0:
            return 0
        ct=0

        for i in range(n):
            prefixsum+=nums[i]
            curmod=prefixsum%p
            target=(curmod-rem+p)%p
            if target in prefixmod:
                n=min(n,i-prefixmod[target])
            prefixmod[curmod]=i
        if n<len(nums):
            return n
        else:
            return -1
