class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sl=sorted(nums)[::-1]
        for i in range(len(nums)-2):
            if sl[i]<sl[i+1]+sl[i+2]:
                return sl[i]+sl[i+1]+sl[i+2]
        
        return 0