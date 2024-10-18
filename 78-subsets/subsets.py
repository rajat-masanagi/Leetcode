class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def subset(i,s):
            if i==len(nums):
                res.append(s)
                return
            subset(i+1,s+[nums[i]])
            subset(i+1,s)

        subset(0,[])
        return res

        