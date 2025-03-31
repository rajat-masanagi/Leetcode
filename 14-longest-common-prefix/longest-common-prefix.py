class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        min_length = min(len(s) for s in strs)
        if min_length == 0:
            return ""

        for i in range(min_length):
            if len(strs[0])==0:
                return ""
            letter=strs[0][i]
            for j in range(1,len(strs)):
                if len(strs[j])==0:
                    return ""
                if strs[j][i]==letter:
                    continue
                else:
                    if i==0:
                        return ""
                    else: 
                        return strs[0][:i]
                        
        return strs[0][:min_length]

