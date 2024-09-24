class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        h=set()
        for i in arr1:
            t=""
            for j in str(i):
                t+=j
                h.add(int(t))
        ans=0
        for i in arr2:
            t=""
            for j in str(i):
                t+=j
                if int(t) in h and len(t)>ans:
                    ans+=1
        return ans