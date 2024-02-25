class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ma=0
        for i in sentences:
            if len(i.split(" "))>ma:
                ma=len(i.split(" "))
        return ma