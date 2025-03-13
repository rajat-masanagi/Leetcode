class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        threshold=len(nums)//2
        count=0
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
                if count>=threshold:
                    return nums[i]
            else:
                count=0