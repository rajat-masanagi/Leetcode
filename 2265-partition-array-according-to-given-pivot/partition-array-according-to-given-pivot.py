class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new_nums=[0]*len(nums)
        pt=0
        for i in range(len(nums)):
            if nums[i] < pivot:
                new_nums[pt]=nums[i]
                pt+=1
        for i in range(len(nums)):
            if nums[i] == pivot:
                new_nums[pt]=nums[i]
                pt+=1
        for i in range(len(nums)):
            if nums[i] > pivot:
                new_nums[pt]=nums[i]
                pt+=1
        return new_nums