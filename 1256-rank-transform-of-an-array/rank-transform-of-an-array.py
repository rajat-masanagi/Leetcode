class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ins=sorted(list(set(arr)))
        d={}
        for i in range(len(ins)):
            d[ins[i]]=i+1
        ans=[1]*len(arr)
        for i in range(len(arr)):
            ans[i]=d[arr[i]]
        return ans
            