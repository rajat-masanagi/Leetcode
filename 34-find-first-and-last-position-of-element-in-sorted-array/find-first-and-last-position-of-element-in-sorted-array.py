class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        lb=-1
        ub=10e10
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                lb=mid
                r=mid-1
            else:
                l=mid+1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<=target:
                ub=mid
                l=mid+1
            else:
                r=mid-1
        if ub==10e10:
            return [-1,-1]
        if nums[lb]!=target or nums[ub]!=target or len(nums)==0:
            return [-1,-1]
        
        return [lb,ub]