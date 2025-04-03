class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxi=0
        dif=0
        i=nums[0]
        for j in range(1,len(nums)-1):
            dif=max(dif,i-nums[j])
            maxi=max(maxi,dif*nums[j+1])
            i=max(i,nums[j])
        return maxi

