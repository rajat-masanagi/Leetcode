class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr=[0]*(len(nums)+1)
        for i in queries:
            arr[i[0]]-=1
            if i[1]+1<len(nums):
                arr[i[1]+1]+=1
        sumi=0
        for i in range(len(nums)):
            sumi+=arr[i]
            if nums[i]>-sumi:
                return False
        return True
