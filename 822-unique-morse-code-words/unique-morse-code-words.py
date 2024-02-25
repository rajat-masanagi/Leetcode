class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[]
        for i in words:
            r=""
            for j in i:
                r=r+morse[ord(j)-ord("a")]
            res.append(r)
        return len(set(res))