class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            if i%3!=0:
                sum+=1
        return sum