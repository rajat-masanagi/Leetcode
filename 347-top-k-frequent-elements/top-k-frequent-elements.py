class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in set(list(d.keys())):
                d[i]+=1
            else:
                d.update({i:1})
        vl=dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        ans=list(vl.keys())[:k]
        return ans