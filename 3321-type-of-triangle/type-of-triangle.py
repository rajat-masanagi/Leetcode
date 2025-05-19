class Solution:
    def triangleType(self, nums: List[int]) -> str:
        se=set(nums)
        if (nums[0]+nums[1])>nums[2] and (nums[0]+nums[2])>nums[1] and (nums[2]+nums[1])>nums[0]:
            if len(se)==1:
                ans="equilateral"
            elif len(se)==2:
                ans="isosceles"
            else:
                ans="scalene"
        else:
            ans="none"
        return ans