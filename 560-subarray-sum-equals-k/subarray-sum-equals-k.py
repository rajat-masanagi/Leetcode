class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        prefix_sum=0
        count=0
        for i in nums:
            if prefix_sum in d:
                d[prefix_sum]+=1
            else:
                d[prefix_sum]=1
            prefix_sum+=i
            if prefix_sum-k in d:
                count+=d[prefix_sum-k]
        return count


                