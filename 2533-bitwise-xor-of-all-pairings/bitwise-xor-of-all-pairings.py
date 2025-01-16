class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans=0
        n1=len(nums1)
        n2=len(nums2)
        for i in nums1:
            if n2%2!=0:
                ans=ans^i
        for j in nums2:
            if n1%2!=0:
                ans=ans^j
        return ans
