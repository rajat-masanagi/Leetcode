from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets=[]
        for i in range(1,len(nums)+1):
            subsets.append(list(combinations(nums,i)))
        ans=0
        for i in subsets:
            for j in i:
                val=0
                for k in j:
                    val=val^k
                ans+=val
        return ans

