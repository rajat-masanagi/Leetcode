class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index_s= {char: i for i,char in enumerate(s)}
        index_t= {char: i for i,char in enumerate (t)}

        return sum(abs(index_s[char]-index_t[char]) for char in s)