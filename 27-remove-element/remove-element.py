class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr=[]
        for i in nums:
            if i !=val:
                arr.append(i)
        nums.clear()
        nums.extend(arr)
        return len(arr)