class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # ans=0
        # for i in nums1:
        #     for j in nums2:
        #         ans=ans^(i^j)
        # return ans
        ans1=0
        ans2=0
        n1=len(nums1)
        n2=len(nums2)
        for i in nums1:
            if n2%2!=0:
                ans1=ans1^i
        for j in nums2:
            if n1%2!=0:
                ans2=ans2^j
        return ans1^ans2
