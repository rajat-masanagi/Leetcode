class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        for i in range(len(nums)):
            if nums[i]==0:
                count0+=1
        pt=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pt]=nums[i]
                pt+=1
        for i in range(len(nums)-1,len(nums)-count0-1,-1):
            nums[i]=0
        

            
                
        