class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0
        for i in range(0, len(nums), 3):
            if len(counts) == len(nums)-i:
                break
            j = i
            while j<i+3 and j<len(nums):
                counts[nums[j]]-=1
                if counts[nums[j]] == 0:
                    del counts[nums[j]]
                j+=1
            ans += 1
        return ans