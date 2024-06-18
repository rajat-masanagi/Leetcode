class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        pt1=0
        pt2=0
        while pt1<len(word1) or pt2<len(word2):
            if pt1<len(word1):
                s=s+word1[pt1]
                pt1=pt1+1
            if pt2<len(word2):
                s=s+word2[pt2]
                pt2=pt2+1
        return s
