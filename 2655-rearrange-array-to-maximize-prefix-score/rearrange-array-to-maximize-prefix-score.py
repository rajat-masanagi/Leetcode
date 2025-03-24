class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        psum=0
        count=0
        for i in nums:
            psum+=i
            if psum>0:
                count+=1
            else:
                break
        return count
