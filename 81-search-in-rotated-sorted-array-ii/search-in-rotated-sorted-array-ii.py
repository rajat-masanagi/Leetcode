class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            print(mid)
            if nums[mid]==target:
                return True
            if nums[mid]==nums[left]:
                left+=1
                continue
            if nums[mid]>nums[left]:
                if nums[left]<=target and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False