import numpy as np
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ina=np.argsort(arr)
        ins=np.sort(arr)
        ans=[1]*len(arr)
        for i in range(1,len(arr)):
            if ins[i-1]==ins[i]:
                ans[ina[i]]=ans[ina[i-1]]
            else:
                ans[ina[i]]=ans[ina[i-1]]+1
        return ans
            