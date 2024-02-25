class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        L=[]
        for i in range(len(words)):
            s=set(words[i])
            if x in s:
                L.append(i)
        return L
