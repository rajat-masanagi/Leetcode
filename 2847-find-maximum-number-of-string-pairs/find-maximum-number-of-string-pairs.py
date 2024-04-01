class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s={""}
        for i in words:
            z=sorted(i)
            s.add(z[0]+z[1])
        return len(words)-len(s)+1