class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def canzero(nums,queries):
            arr=[0]*(len(nums)+1)
            for i in range(len(queries)):
                arr[queries[i][0]]-=queries[i][2]
                arr[queries[i][1]+1]+=queries[i][2]
            
            sumi=0
            for i in range(len(nums)):
                sumi+=arr[i]
                if nums[i]>-sumi:
                    return False
            return True
        
        left=0
        right=len(queries)
        ans=-1
        while left<=right:
            mid=(right+left)//2
            if canzero(nums,queries[:mid])==True:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
