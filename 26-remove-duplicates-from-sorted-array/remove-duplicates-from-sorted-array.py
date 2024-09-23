class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=[]
        i=0
        j=1
        while(j<len(nums)):
            if nums[i]!=nums[j]:
                arr.append(nums[i])
            i+=1
            j+=1
        arr.append(nums[i])
        nums.clear()
        nums.extend(arr)
        return len(arr)
        