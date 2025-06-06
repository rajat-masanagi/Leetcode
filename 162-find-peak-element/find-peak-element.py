class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        elif nums[1]<nums[0]:
            return 0
        elif nums[n-1]>nums[n-2]:
            return n-1
        
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid-1
        return -1