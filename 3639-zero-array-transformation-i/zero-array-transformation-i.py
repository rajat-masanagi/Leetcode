class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr=[0]*(len(nums)+1)
        for i in range(len(queries)):
            arr[queries[i][0]]-=1
            # if queries[i][1]+1<len(nums):
            arr[queries[i][1]+1]+=1
        sumi=0
        for i in range(len(nums)):
            sumi+=arr[i]
            if nums[i]>-sumi:
                return False
        return True
