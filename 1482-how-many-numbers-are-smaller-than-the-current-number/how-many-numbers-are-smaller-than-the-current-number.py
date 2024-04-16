class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=[i,nums[i]]
        nums=sorted(nums,key=lambda x: x[1])
        L=[0]*len(nums)
        for i in range(1,len(nums)):
            if(nums[i-1][1]!=nums[i][1]):
                L[nums[i][0]]=i
            else:
                L[nums[i][0]]=L[nums[i-1][0]]
        return L