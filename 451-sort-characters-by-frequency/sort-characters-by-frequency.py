class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        sorted_keys = sorted(d, key=lambda k: d[k], reverse=True)
        ans=""
        for i in sorted_keys:
            ans+=i*d[i]
        return ans