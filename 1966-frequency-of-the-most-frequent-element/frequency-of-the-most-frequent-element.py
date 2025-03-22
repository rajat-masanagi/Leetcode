class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total=0
        ans=0
        l=0
        r=0
        nums.sort()
        while r<len(nums):
            total+=nums[r]
            while nums[r]*(r-l+1) > total+k:
                total -= nums[l]
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans

