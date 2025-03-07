class Solution:
    def check(self, nums: List[int]) -> bool:
        mini=min(nums)
        idxs=[]
        for i in range(len(nums)):
            if nums[i]==mini:
                idxs.append(i)
        for j in idxs:
            left=[]
            right=[]
            for i in range(len(nums)):
                if i>=j:
                    right.append(nums[i])
                else:
                    left.append(nums[i])
            arr=right+left
            flag=sorted(arr)==arr
            if flag==True:
                return True
        return False