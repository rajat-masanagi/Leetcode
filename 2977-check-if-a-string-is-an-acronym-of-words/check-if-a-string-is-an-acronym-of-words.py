class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        re=""
        for i in words:
            re=re+i[0]
        if re==s:
            return True
        else:
            return False