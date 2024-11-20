class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        flag_0=0
        for i in nums:
            if i!=0:
                product*=i
            elif i==0:
                flag_0+=1
        ans=[]
        for i in nums:
            if i==0:
                ans.append(product)
            if i!=0 and flag_0==0:
                ans.append(product//i)
            if i!=0 and flag_0>0:
                ans.append(0)
        if flag_0>1:
            return [0]*len(nums)
        else:
            return ans