class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res=[]

        def subset(i,s):
            if i==len(nums):
                res.append(s)
                return
            subset(i+1,s+[nums[i]])
            subset(i+1,s)
        
        subset(0,[])
        ans=[]
        maxi=0
        for i in range(len(res)):
            bor=0
            for j in range(len(res[i])):
                bor=bor | res[i][j]
            if bor>=maxi:
                maxi=bor
            ans.append(bor)

        k=0
        for i in ans:
            if i==maxi:
                k+=1

        return k